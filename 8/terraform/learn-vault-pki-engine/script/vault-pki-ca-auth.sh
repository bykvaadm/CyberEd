export VAULT_ADDR="http://127.0.0.1:8200/"
export VAULT_TOKEN="hvs.HZ52ZxoxLFcS2vRjB0cwqErS"



vault policy write engine-policy - <<EOF
# Enable secrets engine
path "sys/mounts/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}

# List enabled secrets engine
path "sys/mounts" {
  capabilities = [ "read", "list" ]
}

# Work with pki secrets engine
path "pki*" {
  capabilities = [ "create", "read", "update", "delete", "list", "sudo" ]
}

EOF

vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

echo "1.3 create root CA"

vault write -field=certificate pki/root/generate/internal \
     common_name="example.com" \
     issuer_name="root-2023" \
     ttl=87600h > root_2023_ca.crt

cat root_2023_ca.crt

echo "1.5"
ISSUER=$(vault list -format=json pki/issuers/ | jq -r '.[]')
vault read pki/issuer/$ISSUER | tail -n 6

echo "1.6"
vault write pki/roles/2023-servers allow_any_name=true

echo "1.7"
vault write pki/config/urls \
     issuing_certificates="$VAULT_ADDR/v1/pki/ca" \
     crl_distribution_points="$VAULT_ADDR/v1/pki/crl"

echo "step 2.1"

vault secrets enable -path=pki_int pki

vault secrets tune -max-lease-ttl=43800h pki_int

echo "2.3 Intermediate Authority"

# original
# vault write -format=json pki_int/intermediate/generate/internal \
#      common_name="example.com Intermediate Authority" \
#      issuer_name="example-dot-com-intermediate" \
#      | jq -r '.data.csr' > pki_intermediate.csr

vault write -format=json pki_int/intermediate/generate/internal \
     common_name="example.com Intermediate Authority" \
     | jq -r '.data.csr' > pki_intermediate.csr

cat pki_intermediate.csr

echo "step 2.4"
vault write -format=json pki/root/sign-intermediate \
     issuer_ref="root-2023" \
     csr=@pki_intermediate.csr \
     format=pem_bundle ttl="43800h" \
     | jq -r '.data.certificate' > intermediate.cert.pem

vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem

# step 3

vault write pki_int/roles/example-dot-com \
     issuer_ref="$(vault read -field=default pki_int/config/issuers)" \
     allowed_domains="example.com" \
     allow_subdomains=true \
     max_ttl="720h"

# step 4

# vault write -format=json pki_int/issue/example-dot-com common_name="test.example.com" ttl="24h"
SERIAL_NUMBER=$(vault write -format=json pki_int/issue/example-dot-com common_name="test.example.com" ttl="24h" | jq -r .data.serial_number)

echo "SN: $SERIAL_NUMBER"
echo "step 5"
vault write pki_int/revoke serial_number=$SERIAL_NUMBER

vault write pki_int/tidy tidy_cert_store=true tidy_revoked_certs=true

# step 7

echo "step 7.1"
echo "rotate root"

vault write pki/root/rotate/internal \
    common_name="example.com" \
    issuer_name="root-2024"

echo "7.2"
vault list pki/issuers

vault write pki/roles/2024-servers allow_any_name=true

echo "step 8.1"

vault write -format=json pki/intermediate/cross-sign \
      common_name="example.com" \
      key_ref="$(vault read pki/issuer/root-2024 \
      | grep -i key_id | awk '{print $2}')" \
      | jq -r '.data.csr' \
      | tee cross-signed-intermediate.csr
# echo "8.2 - sign with older r oot CA"
vault write -format=json pki/issuer/root-2023/sign-intermediate \
      common_name="example.com" \
      csr=@cross-signed-intermediate.csr \
      | jq -r '.data.certificate' | tee cross-signed-intermediate.crt

echo "8.3"

vault write pki/intermediate/set-signed \
      certificate=@cross-signed-intermediate.crt

# echo "8.4 - ca chain"

# vault read pki/issuer/root-2024

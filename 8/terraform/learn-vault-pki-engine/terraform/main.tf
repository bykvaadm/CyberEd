# step 1.1 and 1.2
resource "vault_mount" "pki" {
  path        = "pki"
  type        = "pki"
  description = "This is an example PKI mount"

  default_lease_ttl_seconds = 86400
  max_lease_ttl_seconds     = 315360000
}

# 1.3
# vault write -field=certificate pki/root/generate/internal \
#   common_name="example.com" \
#   issuer_name="root-2023" \
#   ttl=87600h > root_2023_ca.crt

resource "vault_pki_secret_backend_root_cert" "root_2023" {
  backend     = vault_mount.pki.path
  type        = "internal"
  common_name = "example.com"
  ttl         = 315360000
  issuer_name = "root-2023"
}

output "vault_pki_secret_backend_root_cert_root_2023" {
  value = vault_pki_secret_backend_root_cert.root_2023.certificate
}

resource "local_file" "root_2023_cert" {
  content  = vault_pki_secret_backend_root_cert.root_2023.certificate
  filename = "root_2023_ca.crt"
}

# used to update name and properties
# manages lifecycle of existing issuer
resource "vault_pki_secret_backend_issuer" "root_2023" {
  backend                        = vault_mount.pki.path
  issuer_ref                     = vault_pki_secret_backend_root_cert.root_2023.issuer_id
  issuer_name                    = vault_pki_secret_backend_root_cert.root_2023.issuer_name
  revocation_signature_algorithm = "SHA256WithRSA"
}

# 1.6
# vault write pki/roles/2023-servers allow_any_name=true

resource "vault_pki_secret_backend_role" "role" {
  backend          = vault_mount.pki.path
  name             = "2023-servers-role"
  allow_ip_sans    = true
  key_type         = "rsa"
  key_bits         = 4096
  allow_subdomains = true
  allow_any_name   = true
}

# 1.7
resource "vault_pki_secret_backend_config_urls" "config-urls" {
  backend                 = vault_mount.pki.path
  issuing_certificates    = ["http://localhost:8200/v1/pki/ca"]
  crl_distribution_points = ["http://localhost:8200/v1/pki/crl"]
}

# step 2 - 2.1 and 2.2
# vault secrets enable -path=pki_int pki
# vault secrets tune -max-lease-ttl=43800h pki_int

resource "vault_mount" "pki_int" {
  path        = "pki_int"
  type        = "pki"
  description = "This is an example intermediate PKI mount"

  default_lease_ttl_seconds = 86400
  max_lease_ttl_seconds     = 157680000
}

# 2.3 - generate intermediate and save csr
# vault write -format=json pki_int/intermediate/generate/internal \
#      common_name="example.com Intermediate Authority" \
#      issuer_name="example-dot-com-intermediate" \
#      | jq -r '.data.csr' > pki_intermediate.csr

resource "vault_pki_secret_backend_intermediate_cert_request" "csr-request" {
  backend     = vault_mount.pki_int.path
  type        = "internal"
  common_name = "example.com Intermediate Authority"
}

resource "local_file" "csr_request_cert" {
  content  = vault_pki_secret_backend_intermediate_cert_request.csr-request.csr
  filename = "pki_intermediate.csr"
}

# step 2.4
# vault write -format=json pki/root/sign-intermediate \
#      issuer_ref="root-2023" \
#      csr=@pki_intermediate.csr \
#      format=pem_bundle ttl="43800h" \
#      | jq -r '.data.certificate' > intermediate.cert.pem

resource "vault_pki_secret_backend_root_sign_intermediate" "intermediate" {
  backend     = vault_mount.pki.path
  common_name = "new_intermediate"
  csr         = vault_pki_secret_backend_intermediate_cert_request.csr-request.csr
  format      = "pem_bundle"
  ttl         = 15480000
  issuer_ref  = vault_pki_secret_backend_root_cert.root_2023.issuer_id
}

resource "local_file" "intermediate_ca_cert" {
  content  = vault_pki_secret_backend_root_sign_intermediate.intermediate.certificate
  filename = "intermediate.cert.pem"
}

# step 2.5
# vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem

resource "vault_pki_secret_backend_intermediate_set_signed" "intermediate" {
  backend     = vault_mount.pki_int.path
  certificate = vault_pki_secret_backend_root_sign_intermediate.intermediate.certificate
}

# manage the issuer created for the set signed
resource "vault_pki_secret_backend_issuer" "intermediate" {
  backend     = vault_mount.pki_int.path
  issuer_ref  = vault_pki_secret_backend_intermediate_set_signed.intermediate.imported_issuers[0]
  issuer_name = "example-dot-com-intermediate"
}

# vault list pki_int_example/issuer

# step 3
# vault write pki_int/roles/example-dot-com \
#      issuer_ref="$(vault read -field=default pki_int/config/issuers)" \
#      allowed_domains="example.com" \
#      allow_subdomains=true \
#      max_ttl="720h"

resource "vault_pki_secret_backend_role" "intermediate_role" {
  backend          = vault_mount.pki_int.path
  issuer_ref       = vault_pki_secret_backend_issuer.intermediate.issuer_ref
  name             = "example-dot-com"
  ttl              = 86400
  max_ttl          = 2592000
  allow_ip_sans    = true
  key_type         = "rsa"
  key_bits         = 4096
  allowed_domains  = ["example.com"]
  allow_subdomains = true

}

#  step4: request new cert for URL
#  vault write pki_int/issue/example-dot-com common_name="test.example.com" ttl="24h"

resource "vault_pki_secret_backend_cert" "example-dot-com" {
  issuer_ref  = vault_pki_secret_backend_issuer.intermediate.issuer_ref
  backend     = vault_pki_secret_backend_role.intermediate_role.backend
  name        = vault_pki_secret_backend_role.intermediate_role.name
  common_name = "test.example.com"
  ttl         = 3600
  revoke     = true
}

output "vault_pki_secret_backend_cert_example-dot-com_cert" {
  value = vault_pki_secret_backend_cert.example-dot-com.certificate
}

output "vault_pki_secret_backend_cert_example-dot-com_issuring_ca" {
  value = vault_pki_secret_backend_cert.example-dot-com.issuing_ca
}

output "vault_pki_secret_backend_cert_example-dot-com_serial_number" {
  value = vault_pki_secret_backend_cert.example-dot-com.serial_number
#   sensitive = true
}

output "vault_pki_secret_backend_cert_example-dot-com_private_key_type" {
  value = vault_pki_secret_backend_cert.example-dot-com.private_key_type
}

# step 5, expain the revoke = true

# 6 not possible via TF
# step 8 is part of demo

# step 7 create a second root instead of rotate

# vault write pki/root/rotate/internal \
#     common_name="example.com" \
#     issuer_name="root-2024"
#
# Method	Path
# POST	/pki/root/generate/:type
# POST	/pki/issuers/generate/root/:type
# POST	/pki/root/rotate/:type

resource "vault_pki_secret_backend_root_cert" "root_2024" {
  backend     = vault_mount.pki.path
  type        = "internal"
  common_name = "example.com"
  ttl         = "315360000"
  issuer_name = "root-2024"
  key_name    = "root_2024"
}

# used to update name and properties
# manages lifecycle of existing issuer
resource "vault_pki_secret_backend_issuer" "root_2024" {
  backend                        = vault_mount.pki.path
  issuer_ref                     = vault_pki_secret_backend_root_cert.root_2024.issuer_id
  issuer_name                    = vault_pki_secret_backend_root_cert.root_2024.issuer_name
  revocation_signature_algorithm = "SHA256WithRSA"
}

# vault write pki/roles/2024-servers allow_any_name=true
resource "vault_pki_secret_backend_role" "role_2024" {
  backend        = vault_mount.pki.path
  name           = "2024-servers"
  allow_any_name = true
}

# 8.1 - creates a new cross-signed intermediate CSR
# uses key from new root in step 7
# vault write -format=json pki/intermediate/cross-sign \
#       common_name="example.com" \
#       key_ref="$(vault read pki/issuer/root-2024 \
#       | grep -i key_id | awk '{print $2}')" \
#       | jq -r '.data.csr' \
#       | tee cross-signed-intermediate.csr
# pki/intermediate/cross-sign == pki/issuers/generate/intermediate/existing

resource "vault_pki_secret_backend_intermediate_cert_request" "new_csr" {
  backend     = vault_mount.pki.path
  type        = "existing"
  common_name = "example.com"
  key_ref     = vault_pki_secret_backend_root_cert.root_2024.key_name
}

## write to file
resource "local_file" "new_csr_file" {
  content  = vault_pki_secret_backend_intermediate_cert_request.new_csr.csr
  filename = "cross-signed-intermediate.csr"
}

# 8.2 - sign csr with older root CA
# vault write -format=json pki/issuer/root-2023/sign-intermediate \
#       common_name="example.com" \
#       csr=@cross-signed-intermediate.csr \
#       | jq -r '.data.certificate' | tee cross-signed-intermediate.crt

resource "vault_pki_secret_backend_root_sign_intermediate" "root_2024" {
  backend     = vault_mount.pki.path
  csr         = vault_pki_secret_backend_intermediate_cert_request.new_csr.csr
  common_name = "example.com"
  ttl         = 43800
  issuer_ref  = vault_pki_secret_backend_root_cert.root_2023.issuer_id
}

# 8.3
# vault write pki/intermediate/set-signed \
#       certificate=@cross-signed-intermediate.crt

resource "vault_pki_secret_backend_intermediate_set_signed" "root_2024" {
  backend     = vault_mount.pki.path
  certificate = vault_pki_secret_backend_root_sign_intermediate.root_2024.certificate
}

# 8.4 - print 
# vault read pki/issuer/root-2024
output "vault_pki_secret_backend_root_sign_intermediate_root_2024_ca_chain" {
  value = vault_pki_secret_backend_root_sign_intermediate.root_2024.ca_chain
}

# # step 9
# # Set new default issuer
# resource "vault_pki_secret_backend_config_issuers" "config" {
#   backend                       = vault_mount.pki.path
#   default                       = vault_pki_secret_backend_issuer.root_2024.issuer_id
#   default_follows_latest_issuer = true
# }
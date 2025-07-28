# output "root_cert_field" {
#   value = vault_pki_secret_backend_root_cert.root-2023.certificate
# }
# output "root_cert" {
#   value = vault_pki_secret_backend_root_cert.root-2023
# }

# output "ca_urls" {
#   value = "$(var.vault_addr}/v1/pki/crl"

# }

# output "intermediate_csr" {
#   value = vault_pki_secret_backend_intermediate_cert_request.csr-request.csr

# }


# output "signed" {
#   value = vault_pki_secret_backend_root_sign_intermediate.intermediate.certificate
# }
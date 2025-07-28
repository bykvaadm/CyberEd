export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=root

start-vault:
	echo "starting Vault server"
	vault server -dev -dev-root-token-id root

create:
	cd terraform/; terraform init; terraform plan --out tf.plan;terraform apply tf.plan
	cd script/; sh vault-pki-ca-auth.sh

clean:
	rm -rf terraform/.terraform terraform/.terraform.lock.hcl terraform/terraform.tfstate terraform/tf.plan terraform/terraform.tfstate.backup terraform/*.csr terraform/*.crt terraform/*.pem
	rm -rf script/*.csr script/*.crt script/*.pem
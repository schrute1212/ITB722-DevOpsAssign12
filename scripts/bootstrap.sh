#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/terraform"

echo "1) Terraform init & apply"
terraform init
terraform apply -auto-approve

echo "2) Capture outputs"
terraform output -json > ../terraform_outputs.json

echo "3) Generate Ansible inventory"
cd "$ROOT"
python3 ansible/generate_inventory.py

echo "4) Run Ansible to install Docker"
ansible-playbook -i ansible/inventory.ini ansible/playbook_setup.yml

echo "5) Initialize swarm and join workers"
ansible-playbook -i ansible/inventory.ini ansible/playbook_swarm.yml

echo "6) Deploy docker stack"
ansible-playbook -i ansible/inventory.ini ansible/playbook_deploy.yml

echo "Bootstrap complete. Visit: http://<manager_public_ip>:8000"

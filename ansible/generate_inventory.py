#!/usr/bin/env python3
import json
import pathlib
tf_json = pathlib.Path("../terraform_outputs.json")
inv_path = pathlib.Path("inventory.ini")

if not tf_json.exists():
    print("Please run 'terraform output -json > terraform_outputs.json' in terraform/ first")
    exit(1)

data = json.loads(tf_json.read_text())
controller = data["controller_public_ip"]["value"]
manager = data["manager_public_ip"]["value"]
workerA = data["workerA_public_ip"]["value"]
workerB = data["workerB_public_ip"]["value"]

content = f"""[manager]
{manager} ansible_user=ubuntu ansible_ssh_private_key_file=../terraform/terraform-key.pem ansible_host={manager}

[workers]
{workerA} ansible_user=ubuntu ansible_ssh_private_key_file=../terraform/terraform-key.pem ansible_host={workerA}
{workerB} ansible_user=ubuntu ansible_ssh_private_key_file=../terraform/terraform-key.pem ansible_host={workerB}

[controller]
{controller} ansible_user=ubuntu ansible_ssh_private_key_file=../terraform/terraform-key.pem ansible_host={controller}

[all:vars]
ansible_python_interpreter=/usr/bin/python3
"""

inv_path.write_text(content)
print("Created ansible/inventory.ini")

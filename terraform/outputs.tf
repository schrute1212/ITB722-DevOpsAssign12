output "controller_public_ip" {
  value = aws_instance.controller.public_ip
}
output "manager_public_ip" {
  value = aws_eip.manager_eip.public_ip
}
output "workerA_public_ip" {
  value = aws_eip.workerA_eip.public_ip
}
output "workerB_public_ip" {
  value = aws_eip.workerB_eip.public_ip
}
output "private_key_path" {
  value = "${path.module}/terraform-key.pem"
}

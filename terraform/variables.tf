variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "key_name" {
  type    = string
  default = "devops_assignment_key"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "ssh_cidr" {
  type    = string
  default = "0.0.0.0/0" # lab use only; narrow in real world
}

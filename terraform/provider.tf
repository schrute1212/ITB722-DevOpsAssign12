terraform {
  required_providers {
    aws = { source = "hashicorp/aws" }
    tls = { source = "hashicorp/tls" }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

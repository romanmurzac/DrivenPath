provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket = "drivendata-cicd-bucket"
}
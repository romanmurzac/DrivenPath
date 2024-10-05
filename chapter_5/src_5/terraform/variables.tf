variable "account_id" {
  description = "The Account ID of the AWS."
  type        = string
}

variable "region" {
  description = "The region of the DrivenData pipeline."
  type        = string
}

variable "tag" {
  description = "The tag for DrivenData pipeline."
  default     = "driven_data"
}

variable "bucket_name" {
  description = "The name of the S3 bucket."
  type        = string
  default     = "driven-data-bucket"
}

variable "mwaa_name" {
  description = "The name of the MWAA environment."
  type        = string
  default     = "driven-data-airflow-environment"
}

variable "personal_public_ip" {
  description = "The Personal Public IP."
  type        = string
}
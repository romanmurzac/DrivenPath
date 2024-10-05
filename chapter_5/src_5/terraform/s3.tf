#tfsec:ignore:AWS002
#tfsec:ignore:AWS017
#tfsec:ignore:AWS077
resource "aws_s3_bucket" "driven_data_bucket" {
  bucket = var.bucket_name
  tags = {
    Name = var.tag
  }
}

resource "aws_s3_bucket_ownership_controls" "s3_bucket_acl_ownership" {
  bucket = aws_s3_bucket.driven_data_bucket.id
  rule {
    object_ownership = "ObjectWriter"
  }
}

resource "aws_s3_bucket_acl" "s3_bucket_acl" {
  bucket = aws_s3_bucket.driven_data_bucket.id
  acl    = "private"
  depends_on = [aws_s3_bucket_ownership_controls.s3_bucket_acl_ownership]
}

resource "aws_s3_bucket_versioning" "s3_bucket_versioning" {
  bucket = aws_s3_bucket.driven_data_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption_configuration" {
  bucket = aws_s3_bucket.driven_data_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {
  bucket                  = aws_s3_bucket.driven_data_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_object" "copy_dags" {
  for_each = fileset("dags/", "*")
  bucket   = aws_s3_bucket.driven_data_bucket.id
  key      = "dags/${each.value}"
  source   = "dags/${each.value}"
  etag     = filemd5("dags/${each.value}")
}

resource "aws_s3_object" "copy_requirements" {
  for_each = fileset("requirements/", "*")
  bucket   = aws_s3_bucket.driven_data_bucket.id
  key      = each.value
  source   = "requirements/${each.value}"
  etag     = filemd5("requirements/${each.value}")
}

resource "aws_s3_object" "copy_tasks" {
  for_each = fileset("tasks/", "*")
  bucket   = aws_s3_bucket.driven_data_bucket.id
  key      = "tasks/${each.value}"
  source   = "tasks/${each.value}"
  etag     = filemd5("tasks/${each.value}")
}
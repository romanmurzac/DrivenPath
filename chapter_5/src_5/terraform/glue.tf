resource "aws_glue_catalog_database" "driven_data_db" {
  name = "driven_data_db"
  description = "Database for DrivenData data."
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "raw_driven_data_crawler" {
  name          = "raw_driven_data_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for raw data."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/raw/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "staging_dim_address_crawler" {
  name          = "staging_dim_address_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for staging address."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/staging/dim_address/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "staging_dim_date_crawler" {
  name          = "staging_dim_date_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for staging date."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/staging/dim_date/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "staging_dim_finance_crawler" {
  name          = "staging_dim_finance_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for staging finance."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/staging/dim_finance/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "staging_dim_person_crawler" {
  name          = "staging_dim_person_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for raw person."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/staging/dim_person/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_crawler" "staging_fact_network_usage_crawler" {
  name          = "staging_fact_network_usage_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Crawls data in S3 and creates table in Glue database for network usage."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/staging/fact_network_usage/"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_job" "staging_dim_address_glue" {
  name        = "staging_dim_address_glue"
  description = "Glue job to transform data from raw to staging address."
  role_arn    = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/dim_address.py"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_job" "staging_dim_date_glue" {
  name     = "staging_dim_date_glue"
  description = "Glue job to transform data from raw to staging date."
  role_arn = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/dim_date.py"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_job" "staging_dim_finance_glue" {
  name     = "staging_dim_finance_glue"
  description = "Glue job to transform data from raw to staging finance."
  role_arn = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/dim_finance.py"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_job" "staging_dim_person_glue" {
  name     = "staging_dim_person_glue"
  description = "Glue job to transform data from raw to staging person."
  role_arn = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/dim_person.py"
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_glue_job" "staging_fact_network_usage_glue" {
  name     = "staging_fact_network_usage_glue"
  description = "Glue job to transform data from raw to staging network usage."
  role_arn = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/fact_network_usage.py"
  }
  tags = {
    Name = var.tag
  }
}
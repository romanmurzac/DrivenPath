resource "aws_iam_role" "mwaa_execution_role" {
  name               = "mwaa_execution_role"
  description        = "Role for MWAA execution."
  assume_role_policy = templatefile("${path.module}/policies/airflow_assume_role_policy.json.tpl", {})
  tags = {
    Name = var.tag
  }
}

resource "aws_iam_policy" "mwaa_policy" {
  name        = "mwaa_execution_policy"
  description = "Policy for MWAA permissions."

  policy = templatefile("${path.module}/policies/airflow_execution_role_policy.json.tpl", {
    region      = var.region
    account_id  = var.account_id
    bucket_name = var.bucket_name
    mwaa_name   = var.mwaa_name
  })
}

resource "aws_iam_role_policy_attachment" "mwaa_role_policy_attachment" {
  role       = aws_iam_role.mwaa_execution_role.name
  policy_arn = aws_iam_policy.mwaa_policy.arn
}


resource "aws_iam_role" "glue_execution_role" {
  name               = "glue_execution_role"
  description        = "Role for Glue execution." 
  assume_role_policy = templatefile("${path.module}/policies/glue_assume_role_policy.json.tpl", {})
  tags = {
    Name = var.tag
  }
}

resource "aws_iam_policy" "glue_policy" {
  name        = "glue_execution_policy"
  description = "Policy for Glue permissions."

  policy = templatefile("${path.module}/policies/glue_execution_role_policy.json.tpl", {
    bucket_name = var.bucket_name
  })
}

resource "aws_iam_role_policy_attachment" "glue_role_policy_attachment" {
  role       = aws_iam_role.glue_execution_role.name
  policy_arn = aws_iam_policy.glue_policy.arn
}
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
            "Service": [
                "airflow.amazonaws.com",
                "airflow-env.amazonaws.com"
                ]
        },
        "Action": "sts:AssumeRole"
      }
   ]
}
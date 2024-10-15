CREATE TABLE IF NOT EXISTS streaming_layer.streaming_data (
    person_name VARCHAR(50)
    ,user_name VARCHAR(50)
    ,email VARCHAR(50)
    ,personal_number BIGINT
    ,birth_date VARCHAR(50)
    ,address VARCHAR(250)
    ,phone_number VARCHAR(25)
    ,mac_address VARCHAR(20)
    ,ip_address VARCHAR(20)
    ,iban VARCHAR(25)
    ,accessed_at VARCHAR(50)
    ,session_duration INT
    ,download_speed INT
    ,upload_speed INT
    ,consumed_traffic INT
    ,unique_id VARCHAR(50)
);
SELECT 
	COUNT(*) AS null_values
FROM
	bronze_layer.batch_first_load
WHERE
	person_name IS NULL
	OR user_name IS NULL
	OR email IS NULL
	OR personal_number IS NULL
	OR birth_date IS NULL
	OR address IS NULL
	OR phone IS NULL
	OR mac_address IS NULL
	OR ip_address IS NULL
	OR iban IS NULL
	OR accessed_at IS NULL
	OR session_duration IS NULL
	OR download_speed IS NULL
	OR upload_speed IS NULL
	OR consumed_traffic IS NULL
	OR unique_id IS NULL
    
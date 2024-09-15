CREATE TABLE
	silver_layer.dim_person AS
SELECT
	unique_id,
	person_name,
	user_name,
	email,
	phone,
	birth_date,
	personal_number
FROM
	bronze_layer.batch_first_load

CREATE TABLE
	silver_layer.dim_address AS
SELECT
	unique_id,
	address,
	mac_address,
	ip_address
FROM
	bronze_layer.batch_first_load

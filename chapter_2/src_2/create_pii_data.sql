CREATE TABLE
	golden_layer.pii_data AS
SELECT
	dp.person_name,
	dp.user_name,
	dp.email,
	dp.personal_number, 
	dp.birth_date, 
	da.address,
	dp.phone, 
	da.mac_address,
	da.ip_address,
	df.iban,
	dd.accessed_at,
	fnu.session_duration,
	fnu.download_speed,
	fnu.upload_speed,
	fnu.consumed_traffic,
	fnu.unique_id
FROM
	silver_layer.fact_network_usage fnu
INNER JOIN
	silver_layer.dim_address da ON fnu.unique_id = da.unique_id
INNER JOIN
	silver_layer.dim_date dd ON da.unique_id = dd.unique_id
INNER JOIN
	silver_layer.dim_finance df ON dd.unique_id = df.unique_id
INNER JOIN
	silver_layer.dim_person dp ON df.unique_id = dp.unique_id
    
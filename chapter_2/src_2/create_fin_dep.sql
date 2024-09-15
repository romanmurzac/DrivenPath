CREATE TABLE
	golden_layer.payment_data AS
SELECT
	fnu.unique_id,
	df.iban,
	fnu.download_speed,
	fnu.upload_speed,
	fnu.session_duration,
	fnu.consumed_traffic,
	((fnu.download_speed + fnu.upload_speed + 1)/2) + (fnu.consumed_traffic / (fnu.session_duration + 1)) AS payment_amount
FROM
	silver_layer.fact_network_usage fnu
JOIN
	silver_layer.dim_finance df
ON
	fnu.unique_id = df.unique_id
    
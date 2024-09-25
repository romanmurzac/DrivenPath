{{ config(
    materialized='table',
    schema='trusted',
    alias='non_pii_data',
    tags=['trusted']
) }}

WITH source_data AS (
    SELECT
        '***MASKED***' AS person_name,
        SUBSTRING(dp.user_name, 1, 5) || '*****'  user_name,
        SUBSTRING(dp.email, 1, 5) || '*****' AS email,
        '***MASKED***'  AS personal_number, 
        '***MASKED***' AS birth_date, 
        '***MASKED***' AS address,
        '***MASKED***'  AS phone, 
        SUBSTRING(da.mac_address, 1, 5) || '*****' AS mac_address,
        SUBSTRING(da.ip_address, 1, 5) || '*****' AS ip_address,
        SUBSTRING(df.iban, 1, 5) || '*****' AS iban,
        dd.accessed_at,
        fnu.session_duration,
        fnu.download_speed,
        fnu.upload_speed,
        fnu.consumed_traffic,
        fnu.unique_id
    FROM
        {{ source('staging_source', 'fact_network_usage') }} fnu
    INNER JOIN
        {{ source('staging_source', 'dim_address') }} da ON fnu.unique_id = da.unique_id
    INNER JOIN
        {{ source('staging_source', 'dim_date') }} dd ON da.unique_id = dd.unique_id
    INNER JOIN
        {{ source('staging_source', 'dim_finance') }} df ON dd.unique_id = df.unique_id
    INNER JOIN
        {{ source('staging_source', 'dim_person') }} dp ON df.unique_id = dp.unique_id
)

SELECT
    *
FROM
    source_data
    
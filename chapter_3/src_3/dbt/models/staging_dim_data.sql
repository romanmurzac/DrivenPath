{{ config(
    materialized='table',
    schema='staging',
    alias='dim_data'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        accessed_at
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
    
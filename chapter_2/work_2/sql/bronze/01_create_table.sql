CREATE TABLE IF NOT EXISTS bronze_layer.batch_first_load
(
    person_name character varying(100) COLLATE pg_catalog."default",
    user_name character varying(100) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    personal_number numeric,
    birth_date character varying(100) COLLATE pg_catalog."default",
    address character varying(100) COLLATE pg_catalog."default",
    phone character varying(100) COLLATE pg_catalog."default",
    mac_address character varying(100) COLLATE pg_catalog."default",
    ip_address character varying(100) COLLATE pg_catalog."default",
    iban character varying(100) COLLATE pg_catalog."default",
		accessed_at time without time zone,
    session_duration integer,
    download_speed integer,
    upload_speed integer,
    consumed_traffic integer,
    unique_id character varying(100) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS bronze_layer.batch_first_load
    OWNER to admin;

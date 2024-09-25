SELECT table_schema, table_name
FROM information_schema.tables
where table_schema = 'Sales' and table_type = 'BASE TABLE' ;
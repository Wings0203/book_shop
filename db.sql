CREATE OR REPLACE FUNCTION get_databases(dbname varchar)
RETURNS integer
AS $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_database WHERE datname=dbname)THEN
return 0;
ELSE
return -1;
END IF;
END
$$ LANGUAGE plpgsql;

CREATE EXTENSION IF NOT EXISTS dblink;

CREATE OR REPLACE FUNCTION f_create_db(dbname text)
  RETURNS void AS
$func$
BEGIN
IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
   RAISE NOTICE 'Database already exists';
ELSE
   PERFORM dblink_exec('dbname=' || current_database()
                     , 'CREATE DATABASE ' || quote_ident(dbname));
END IF;

END
$func$ LANGUAGE plpgsql;
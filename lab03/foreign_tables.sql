REATE OR REPLACE FUNCTION create_external_tables()
  RETURNS VOID AS
$$
DECLARE
  file_name TEXT;
BEGIN
  -- Создание схемы "external" если ее не существует
  IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'external') THEN
    CREATE SCHEMA external;
  END IF;
 
  -- Получение списка CSV файлов из директории
  FOR file_name IN
    (SELECT f.filename
     FROM pg_catalog.pg_ls_dir('/home/postgres/data/lab02/output') AS f(filename)
     WHERE f.filename LIKE '%.csv'
    )
  LOOP
    -- Создание внешней таблицы с именем, соответствующим имени файла без расширения
    EXECUTE format('CREATE FOREIGN TABLE external.%I (mounth INTEGER, day INTEGER, year INTEGER, temperature DOUBLE PRECISION) SERVER file_server OPTIONS (filename ''/home/postgres/data/lab02/output/%s'', format ''csv'')',
                   substring(file_name FROM 1 FOR position('.' IN file_name) - 1),
                   file_name
    );
  END LOOP;
END;
$$ LANGUAGE plpgsql;

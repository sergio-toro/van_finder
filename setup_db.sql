#sudo apt-get install python-pip python3-dev libpq-dev postgresql postgresql-contrib
#sudo su - postgres
#psql

CREATE DATABASE van_finder;
CREATE USER van_finder WITH PASSWORD '123456';

ALTER ROLE van_finder SET client_encoding TO 'utf8';
ALTER ROLE van_finder SET default_transaction_isolation TO 'read committed';
ALTER ROLE van_finder SET timezone TO 'Europe/Madrid';

GRANT ALL PRIVILEGES ON DATABASE van_finder TO van_finder;

#\q
#exit
# van_finder

## Install dependencies 
- Install pip ubuntu `sudo apt install python-pip`
- Install virtualenv `pip install virtualenv`
- Install postgres http://tecadmin.net/install-postgresql-server-on-ubuntu/
- `sudo apt-get install postgresql python-psycopg2 libpq-dev python3-dev build-essential libssl-dev libffi-dev python-dev`

## Install project
- `git clone https://github.com/sergio-toro/van_finder.git`
- `cd van_finder`
- `virtualenv -p /usr/bin/python3 ./`
- `source ./bin/activate`
- `pip install -r requirements.txt`
- **Setup DB:**
  - `sudo su - postgres`
  - `cd /path/to/van_finder`
  - `psql -f setup_db.sql`

## Init django app
- Activate virtualenv `source ./bin/activate`
- First time run migrations `python manage.py migrate`
- Start server `python manage.py runserver`

## Populate app with spider results
- Activate virtualenv `source ./bin/activate`
- Run all spiders `scrapy crawlall`

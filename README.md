Times Plus Dataviz
==================

This is a little project to show some data collected from my usage of the Times Plus car sharing program in Tokyo.

Requirements
------------

This application is developed on Python 3 and was not tested with Python 2. The requirements are managed with pip-tools. Use `pip-compile` and `pip-sync` to install the required packages as well as `pip-compile --upgrade` to stay up to date.

Running
-------

Running the server needs some basic environment variables set. Postgres has the some defaults for development use, but you must have `MAPBOX_KEY` set to see any maps.

Installation
------------

After install, remember to run these commands to setup the app:

- `python manage.py migrate` -- you need a database with postgis enabled
- `python manage.py collectstatics`
- `python manage.py getstations` to grab the stations (should schedule to run once a week)
- `python manage.py getbookings & python manage.py matchstations` to grab bookings and match them with station info (should schedule to run once a day)

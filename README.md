# Foobar

Python calculator API

## Installation and Setup

Setup a virtual environment using python 3 (3.6.9+ preferably)
Feel free to use any virtualenv tool you're accustomed to (e.g. pipenv)

```
python3 -m venv
```

Activate the virtualenv `source env/bin/activate`

Install the project requirements `pip install requirements.txt`


## Running locally

To get the server running locally:
- Apply the default django migrations `python manage.py migrate`
- Run the server by using `python manage.py runserver`

NOTE: Since this is a demo project with no dedicated database for local work and you will automagically be using sqlite
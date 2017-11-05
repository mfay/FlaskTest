#!/bin/bash

#FLASK_APP=app/app.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0
#FLASK_APP=app/setup.py FLASK_DEBUG=1 python -m flask run

export DATABASE_URL=mysql+pymysql://root:toor@192.168.99.100/sample
export FLASK_APP=flaskr
export FLASK_DEBUG=true
pip install -e ./app
flask run
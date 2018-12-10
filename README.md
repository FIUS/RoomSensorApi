# RoomSensorApi
A small python api for reading the sensors in the FIUS room

## Prerequesits
- python 3.6
- pip [python 3.6]
- venv [python 3.6]

## Preparations:
```shell
# setup virtualenv
python3.6 -m venv venv
. venv/bin/activate


# install requirements
pip install -r requirements_developement.txt
pip install -r requirements.txt

pip install -e .
```

## Start server for development:

First start:
```shell
. venv/bin/activate
export FLASK_APP=room_sensor_api
export FLASK_DEBUG=1  # to enable autoreload
export MODE=debug
# export MODE=production
# export MODE=test

# start server
flask run
```

Subsequent starts:
```shell
flask run
```

## Installing in a Production Environment
See flask wsgi documentation. The preparations as shown above are required.
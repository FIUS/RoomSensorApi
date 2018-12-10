"""
Room sensor api init file.
"""
from sys import platform

from os import environ, path
from logging import getLogger, Logger
from logging.config import dictConfig

from flask import Flask, logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData
from flask_cors import CORS, cross_origin

APP = Flask(__name__, instance_relative_config=True)  # type: Flask
APP.config['MODE'] = environ['MODE'].upper()
if APP.config['MODE'] == 'PRODUCTION':
    APP.config.from_object('room_sensor_api.config.ProductionConfig')
elif APP.config['MODE'] == 'DEBUG':
    APP.config.from_object('room_sensor_api.config.DebugConfig')
elif APP.config['MODE'] == 'TEST':
    APP.config.from_object('room_sensor_api.config.TestingConfig')

APP.config.from_pyfile('/etc/room_sensor_api.conf', silent=True)
APP.config.from_pyfile('room_sensor_api.conf', silent=True)
if ('CONFIG_FILE' in environ):
    APP.config.from_pyfile(environ.get('CONFIG_FILE', 'room_sensor_api.conf'), silent=True)

CONFIG_KEYS = ('BUTTON_PIN')
for env_var in CONFIG_KEYS:
    APP.config[env_var] = environ.get(env_var, APP.config.get(env_var))

dictConfig(APP.config['LOGGING'])

APP.logger.debug('Debug logging enabled')

# Setup Headers
CORS(APP)

# pylint: disable=C0413
from . import routes
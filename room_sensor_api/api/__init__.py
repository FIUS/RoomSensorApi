"""
Main API Module
"""
from flask import Blueprint
from flask_restplus import Api
from .. import APP

API_BLUEPRINT = Blueprint('api', __name__)

API = Api(API_BLUEPRINT, version='0.1', title='Room Sensor API', doc='/doc/',
          description='The Fius Room Sensor API.')

from . import root, openClose

APP.register_blueprint(API_BLUEPRINT)
"""
This module contains all API endpoints for the namespace 'open_close'
"""

from flask_restplus import Resource
from gpiozero import Button

from .. import APP
from . import API
from .models import OPEN_CLOSE

PATH = '/open_close'
ANS = API.namespace('open_close', description='OpenClose', path=PATH)

button = Button(APP.config["BUTTON_PIN"])

@ANS.route('/')
class OpenClose(Resource):
    """
    Open close root element
    """

    @API.marshal_with(OPEN_CLOSE)
    def get(self):
        """
        Get the current open close state
        """
        return {"open" : (not button.is_pressed)}
#        return {"open" : True}
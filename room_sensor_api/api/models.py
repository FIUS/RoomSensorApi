"""
Module containing models for whole API to use.
"""

from flask_restplus import fields
from . import API
from ..hal_field import HaLUrl, UrlData, NestedFields


ID = API.model('Id', {
    'id': fields.Integer(min=1, example=1, readonly=True),
})

ROOT_LINKS = API.model('RootLinks', {
    'self': HaLUrl(UrlData('api.default_root_resource')),
    'open_close': HaLUrl(UrlData('api.open_close_open_close')),
})

ROOT_MODEL = API.model('RootModel', {
    '_links': NestedFields(ROOT_LINKS),
})

OPEN_CLOSE_LINKS = API.model('OpenCloseLinks', {
    'self': HaLUrl(UrlData('api.open_close_open_close')),
})

OPEN_CLOSE = API.model('OpenClose', {
    'open': fields.Boolean,
    '_links': NestedFields(OPEN_CLOSE_LINKS),
})

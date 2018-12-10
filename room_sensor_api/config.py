"""Module containing default config values."""
import logging

class Config(object):
    DEBUG = False
    TESTING = False
    RESTPLUS_VALIDATE = True
    LOGGING = {
        'version': 1,
        'formatters': {
            'extended': {
                'format': '%(asctime)s [%(levelname)s] [%(name)-16s] %(message)s <%(module)s, \
                 %(funcName)s, %(lineno)s; %(pathname)s>',
            },
            'short': {
                'format': '[%(asctime)s] [%(levelname)s] [%(name)-16s] %(message)s',
            }
        },
        'handlers': {
            'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'extended',
                'filename': '/tmp/roomSensorAPI-default.log',
                'maxBytes': 104857600,
                'backupCount': 10,
            },
            'console': {
                'class' : 'logging.StreamHandler',
                'formatter': 'extended',
            }
        },
        'loggers': {
            'flask.app': {
                'level': logging.INFO,
                'propagate': True,
                'handlers': ['default'],
            },
        },
        'root': {
            'level': logging.WARNING,
            'handlers': ['default'],
        },
        'disable_existing_loggers': True,
    }

    BUTTON_PIN = 21

    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    RESTPLUS_JSON = {'indent': None}


class ProductionConfig(Config):
    pass


class DebugConfig(Config):
    DEBUG = True

    Config.LOGGING['loggers']['flask.app']['level'] = logging.DEBUG
    Config.LOGGING['root']['handlers'].append('console')


class TestingConfig(Config):
    TESTING = True

"""
Setup
"""
from setuptools import setup

setup(
    name='room_sensor_api',
    packages=['room_sensor_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_cors',
        'gpiozero',
    ],
)

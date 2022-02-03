#!/usr/bin/python3
""" 
Flask Blueprint
"""

from flask import Blueprint

app_views = Blueprint('__init__', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
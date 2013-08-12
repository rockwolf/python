#!/usr/local/bin/python

"""
See LICENSE file for copyright and license details.
"""

"""
Cece = CEntral Command Entity
"""

from flask import Flask
from cece import views
from modules.constant import *

app = Flask(__name__)
app.config.from_object('config')

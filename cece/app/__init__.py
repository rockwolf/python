#!/usr/env/python
"""
See LICENSE file for copyright and license details.
"""

"""
Cece = CEntral Command Entity
"""

from flask import Flask

#import sys
#sys.path.append('modules')
#from app.modules.constant import *

app = Flask(__name__)
#app.config.from_object('config')

from app import views

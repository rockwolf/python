#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = '3124534675689780'

dbuser = 'rockwolf'
dbpass = ''
dbhost = 'testdb'
dbname = 'finance'
SQLALCHEMY_DATABASE_URI = 'postgresql://'
                + dbuser
                + ':'
                + dbpass
                + '@'
                + dbhost
                + '/'
                + dbname
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database')

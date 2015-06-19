from flask import Flask, render_template, session, request, abort
#from app import Views #TODO: move all the routes to views.py
from forms import FormLeveragedContracts
import sys

app = Flask(__name__)
app.config.from_object('config')


def adjust_system_path():
        """
            Adjust the system path, so we can search in custom dirs for modules.
        """
        sys.path.append('fade/')
        sys.path.append('fade/static/')
        sys.path.append('fade/static/img/')
        sys.path.append('fade/static/js/')
        sys.path.append('fade/static/css/')
        sys.path.append('fade/templates/')
        sys.path.append('instance/')

if __name__ == '__main__':
    adjust_system_path()
    app.run(debug=True)

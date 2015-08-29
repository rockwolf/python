#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template
#from ..forms import FormLeveragedContracts, FormTradingJournal, FormAccount, FormAccountEdit
from src import app, db

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
@home.route('/home/')
def render_home():
    """
        Renders the index page.
    """
    l_user = 'admin'
    l_message = 'Welcome!'
    return render_template('home/index.tpl', p_user = l_user, p_message = l_message)

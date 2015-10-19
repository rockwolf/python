#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template, session, request, abort, redirect
from ..models import TAccount
from ..forms import FormTest
from src import app, db
from sqlalchemy import distinct

# This is a playground for testing new code.

test = Blueprint('test', __name__)

@test.route('/test', methods = ['GET', 'POST'])
@test.route('/test/', methods = ['GET', 'POST'])
@test.route('/test/<id>', methods = ['GET', 'POST'])
def render_test(id = None):
    """
        Renders the test page.
    """
    #l_account_id = TAccount.query.get_or_404(account_id)
    l_accounts = TAccount.query.filter_by(is_active=1).all()
    l_form = FormTest()
    if l_form.validate_on_submit():
        return render_template('test/test.tpl', p_form = l_form, p_accounts = l_accounts)
    return render_template('test/test.tpl', p_form = l_form, p_accounts = l_accounts)

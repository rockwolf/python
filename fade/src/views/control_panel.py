#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template, session, request, abort, redirect
from ..forms import FormAccount
from ..models import TAccount
from src import app, db
from sqlalchemy import distinct

control_panel = Blueprint('control_panel', __name__)

@control_panel.route('/account', methods = ['GET', 'POST'])
@control_panel.route('/account/', methods = ['GET', 'POST'])
@control_panel.route('/account/<account_id>', methods = ['GET', 'POST'])
@control_panel.route('/account/<account_id>/', methods = ['GET', 'POST'])
def render_account(account_id = None):
    """
        Renders the account page.
    """
    l_form = FormAccount(request.form)
    l_accounts = TAccount.query.filter_by(is_active=1).all()
    l_accounts_total = TAccount.query.count()
    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    if request.method == "POST":
        #if l_form.account_id.data:
        l_account = TAccount.query.get_or_404(account_id)
        # or: l_account = TAccount.query.get(l_form.account_id.data)
        l_form = FormAccount(request.form, obj=l_account)
        if l_form.validate_on_submit():
            #l_account = request.form['account_id']
            l_form.populate_obj(l_account)
            return render_template(
                'control_panel/account.tpl',
                p_form = l_form,
                p_accounts = l_accounts,
                p_accounts_total = l_accounts_total,
                p_accounts_distinct = l_accounts_distinct,
                p_accounts_has_double = l_accounts_has_double)
        else:
            print '======== form not validated - account_id = {}'.format(account_id)
    return render_template(
        'control_panel/account.tpl',
        p_form = l_form,
        p_accounts = l_accounts,
        p_accounts_total = l_accounts_total,
        p_accounts_distinct = l_accounts_distinct,
        p_accounts_has_double = l_accounts_has_double)

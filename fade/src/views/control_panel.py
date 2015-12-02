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
    print "TEST 1 ---",
    print account_id
    print "TEST 2 ---",
    print l_form.data
    print "TEST 3 ---",
    print l_form.account_id
    print "TEST 4 ---",
    print l_form.data["account_id"]
    l_accounts = TAccount.query.filter_by(is_active=1).all()
    l_accounts_total = TAccount.query.count()
    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    if request.method == "POST":
        #if l_form.account_id.data:
        #l_account = TAccount.query.get_or_404(l_form.data["hidden_account_id"])
        l_account = TAccount.query.get(account_id)
        l_form = FormAccount(obj=l_account)
        if l_form.validate_on_submit():
            #l_account = request.form['account_id']
            l_form.populate_obj(l_account)
            return render_template(
                'control_panel/account.tpl',
                p_form = l_form,
                p_account_id = account_id,
                p_accounts = l_accounts,
                p_accounts_total = l_accounts_total,
                p_accounts_distinct = l_accounts_distinct,
                p_accounts_has_double = l_accounts_has_double)
        else:
            print '======== form not validated - account_id = {}'.format(account_id)
    else:
        for account in l_accounts:
            l_account = TAccount.query.get(account.account_id)
            l_form = FormAccount(obj=l_account)
            l_form.populate_obj(account)
            # Note: the above works. Check the accounts.tpl.
            # I made the name a p_form.name and it gets filled in!
            # Note2: Something still seems wrong though. It fills in the same value for all lines?
        return render_template(
            'control_panel/account.tpl',
            p_form = l_form,
            p_account_id = account_id,
            p_accounts = l_accounts,
            p_accounts_total = l_accounts_total,
            p_accounts_distinct = l_accounts_distinct,
            p_accounts_has_double = l_accounts_has_double)

# TODO: create delete and add code

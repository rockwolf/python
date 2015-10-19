#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template, session, request, abort, redirect
from ..forms import FormAccount, FormAccountEdit
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
    l_accounts = TAccount.query.filter_by(is_active=1).all()
    l_form = FormAccount(request.form)
    l_accounts_total = TAccount.query.count()
    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    if request.method == "POST":
        l_account = TAccount.query.get_or_404(account_id)
        l_form = FormAccount(request.form, account_id=l_account)

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

    #@control_panel.route('/account/edit', methods = ['POST'])
    #@control_panel.route('/account/edit/', methods = ['POST'])
    #@control_panel.route('/account/edit/<account_id>/', methods = ['POST'])
    #@control_panel.route('/account/edit/<account_id>', methods = ['POST'])
    #@control_panel.route('/account/edit/<account_id>/', methods = ['POST'])
    #def render_account_edit(account_id = None):
    #    """
    #        Renders the account page in edit mode,
    #        for the given account_id.
    #    """
    #    #if request.method == 'GET':
    #    #    return redirect('/account')
    #
    #    l_accounts = TAccount.query.filter_by(is_active=1).all()
    #    print account_id
    #    if account_id is not None:
    #        l_account = TAccount.query.get_or_404(account_id)
    #    l_form = FormAccountEdit(request.form, obj=l_account)
    #    l_accounts_total = TAccount.query.count()
    #    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    #    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    #    if l_form.validate_on_submit():
    #        l_account = request.form['p_account_id']
    #        l_form.populate_obj(l_account)
    #        return render_template(
    #            'control_panel/account.tpl',
    #            p_form = l_form,
    #            p_accounts = l_accounts,
    #            p_accounts_total = l_accounts_total,
    #            p_accounts_distinct = l_accounts_distinct,
    #            p_accounts_has_double = l_accounts_has_double)
    #    return render_template(
    #        'control_panel/index.tpl',
    #        p_form = l_form,
    #        p_accounts = l_accounts,
    #        p_accounts_total = l_accounts_total,
    #        p_accounts_distinct = l_accounts_distinct,
    #        p_accounts_has_double = l_accounts_has_double)

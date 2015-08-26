#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import render_template, session, request, abort, redirect
from forms import FormLeveragedContracts, FormTradingJournal, FormAccount, FormAccountEdit
from models import TAccount
from src import app, db
from ctypes import cdll
from sqlalchemy import distinct


lcf = cdll.LoadLibrary('calculator_finance.so')


@app.route('/')
@app.route('/home')
@app.route('/home/')
def render_home():
    """
        Renders the index page.
    """
    l_user = 'admin'
    l_message = 'Welcome!'
    return render_template('index.tpl', p_user = l_user, p_message = l_message)


@app.route('/leverage', methods = ['GET', 'POST'])
@app.route('/leverage/', methods = ['GET', 'POST'])
def render_leverage():
    """
        Renders the leverage page.
    """
    l_form = FormLeveragedContracts()
    if l_form.validate_on_submit():
        l_leveraged_contracts = lcf.calculate_leveraged_contracts(int(request.form['p_contracts']))
        return render_template('leverage.tpl', p_form = l_form, p_leveraged_contracts = l_leveraged_contracts)
    return render_template('leverage.tpl', p_form = l_form)

@app.route('/tradingjournal', methods = ['GET', 'POST'])
@app.route('/tradingjournal/', methods = ['GET', 'POST'])
def render_tradingjournal():
    """
        Renders the trading journal page.
    """
    l_form = FormTradingJournal()
    if l_form.validate_on_submit():
        l_trade_id = request.form['p_trade_id']
        return render_template('leverage.tpl', p_form = l_form, p_leveraged_contracts = l_leveraged_contracts)
    return render_template('tradingjournal.tpl', p_form = l_form)

@app.route('/account', methods = ['GET', 'POST'])
@app.route('/account/', methods = ['GET', 'POST'])
#@app.route('/account/edit/<account_id>', methods = ['GET', 'POST'])
@app.route('/account/<account_id>', methods = ['GET', 'POST'])
def render_account(account_id = None):
    """
        Renders the account page.
    """
    l_account = None
    l_accounts = TAccount.query.filter_by(is_active=1).all()
    if account_id:
        l_account = TAccount.query.get_or_404(account_id)
    l_form = FormAccount(obj=l_account)
    l_accounts_total = TAccount.query.count()
    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    if l_form.validate_on_submit():
        #l_account_id = request.form['p_account_id']
        #return redirect('/account/edit/', account_id = 5)
        #return redirect('/account/edit/', account_id = 5)
        l_account = int(request.form['hidden_account_id'])
        #l_form.populate_obj(l_account)
        return render_template(
            'account.tpl',
            p_form = l_form,
            p_accounts = l_accounts,
            p_accounts_total = l_accounts_total,
            p_accounts_distinct = l_accounts_distinct,
            p_accounts_has_double = l_accounts_has_double,
            account_id = l_account)
        # TODO: find out how to get the account_id we are editing.

    return render_template(
        'account.tpl',
        p_form = l_form,
        p_accounts = l_accounts,
        p_accounts_total = l_accounts_total,
        p_accounts_distinct = l_accounts_distinct,
        p_accounts_has_double = l_accounts_has_double)


    #@app.route('/account/edit/<account_id>', methods = ['GET', 'POST'])
    #@app.route('/account/edit/<account_id>/', methods = ['GET', 'POST'])
    #def render_account_edit(account_id):
    #    """
    #        Renders the account page in edit mode,
    #        for the given account_id.
    #    """
    #    # Note: We can only populate the fields on a post-request.
    #    # When not in a post request, show the reqular account screen.
    #    # This way, edit must be pressed, to modify. No edit = no account_id
    #    # = we return to the readonly view of the /account page.
    #    if request.method == 'GET':
    #        return redirect('/account')
    #    l_accounts = TAccount.query.filter_by(is_active=1).all()
    #    #l_account = TAccount.query.filter_by(account_id=account_id).first
    #    l_account = TAccount.query.get_or_404(account_id)
    #    l_form = FormAccountEdit(obj=l_account)
    #    l_accounts_total = TAccount.query.count()
    #    l_accounts_distinct = db.session.query(distinct(TAccount.name)).count()
    #    l_accounts_has_double = (l_accounts_total != l_accounts_distinct)
    #    if l_form.validate_on_submit():
    #        l_form.populate_obj(l_account) # why can't I  do this outside of the validate_on_submit?
    #        # TODO: find a way or change the standard form on edit to contain
    #        # pure-edit boxes... but then I need a new var to let the template
    #        # know I'm editing (like a boolean field or something)
    #        # although than I would need 3 types: non-edit - edit on get (pure-edit) -
    #        # edit from form???
    #        return render_template(
    #            'account.tpl',
    #            p_form = l_form,
    #            p_accounts = l_accounts,
    #            p_accounts_total = l_accounts_total,
    #            p_accounts_distinct = l_accounts_distinct,
    #            p_accounts_has_double = l_accounts_has_double)
    #    return render_template(
    #        'account.tpl',
    #        p_form = l_form,
    #        p_accounts = l_accounts,
    #        p_accounts_total = l_accounts_total,
    #        p_accounts_distinct = l_accounts_distinct,
    #        p_accounts_has_double = l_accounts_has_double)
    # 

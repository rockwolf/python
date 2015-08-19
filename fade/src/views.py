#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import render_template, session, request, abort
from forms import FormLeveragedContracts, FormTradingJournal, FormAccount
from models import TAccount
from src import app
from ctypes import cdll


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
def render_account():
    """
        Renders the account page.
    """
    l_form = FormAccount()
    l_accounts = TAccount.query.all() #filter_by(is_active=True) doesn't work?
    l_accounts_total = TAccount.query.count()
    l_accounts_distinct = TAccounts.query(name).group_by(name).count()
    if l_form.validate_on_submit():
        return render_template(
            'account.tpl',
            p_form = l_form,
            p_accounts = l_accounts,
            p_accounts_total = l_accounts_total,
            p_accounts_distinct = l_accounts_distinct)
    return render_template(
        'account.tpl',
        p_form = l_form,
        p_accounts = l_accounts,
        p_accounts_total = l_accounts_total,
        p_accounts_distinct = l_accounts_distinct)
    #if l_form.validate_on_submit():
    #    return render_template('account.tpl', p_form = l_form, p_accounts = l_accounts, p_account_changed = True)
    #return render_template('account.tpl', p_form = l_form, p_accounts = l_accounts, p_account_changed = False)

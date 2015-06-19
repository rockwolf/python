#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import render_template, session, request, abort
from forms import FormLeveragedContracts
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

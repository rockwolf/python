#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template, session, request, abort, redirect
from ..forms import FormLeveragedContracts, FormTradingJournal
from src import app, db
from ctypes import cdll
from sqlalchemy import distinct


lcf = cdll.LoadLibrary('calculator_finance.so')

finance = Blueprint('finance', __name__)

@finance.route('/leverage', methods = ['GET', 'POST'])
@finance.route('/leverage/', methods = ['GET', 'POST'])
def render_leverage():
    """
        Renders the leverage page.
    """
    l_form = FormLeveragedContracts()
    if l_form.validate_on_submit():
        l_leveraged_contracts = lcf.calculate_leveraged_contracts(int(request.form['p_contracts']))
        return render_template('finance/leverage.tpl', p_form = l_form, p_leveraged_contracts = l_leveraged_contracts)
    return render_template('finance/leverage.tpl', p_form = l_form)

@finance.route('/tradingjournal', methods = ['GET', 'POST'])
@finance.route('/tradingjournal/', methods = ['GET', 'POST'])
def render_tradingjournal():
    """
        Renders the trading journal page.
    """
    l_form = FormTradingJournal()
    if l_form.validate_on_submit():
        l_trade_id = request.form['p_trade_id']
        return render_template('finance/leverage.tpl', p_form = l_form, p_leveraged_contracts = l_leveraged_contracts)
    return render_template('finance/tradingjournal.tpl', p_form = l_form)

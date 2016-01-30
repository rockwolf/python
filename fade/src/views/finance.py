#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask import Blueprint, render_template, session, request, abort, redirect
from ..forms import FormLeveragedContracts, FormTradingJournal, FormDrawdown, FormAveragePrice
from src import app, db
from ctypes import cdll, Structure, c_int, c_double
from sqlalchemy import distinct


lcf = cdll.LoadLibrary('libcalculatorfinance.so')

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


@finance.route('/drawdown', methods = ['GET', 'POST'])
@finance.route('/drawdown/', methods = ['GET', 'POST'])
def render_drawdown():
    """
        Renders the drawdown page.
    """
    # TODO: testing and correcting
    l_form = FormDrawdown()
    if l_form.validate_on_submit():
        return render_template('finance/drawdown.tpl', p_form = l_form)
    return render_template('finance/drawdown.tpl', p_form = l_form)
    
class SharesPrice(Structure):
    """
        Class to represent a C SharesPrice struct,
        as found in libcalculatorfinance.so.
    """
    _fields_ = [
        ("sp_shares", c_int),
        ("sp_price", c_double)]

@finance.route('/averageprice', methods = ['GET', 'POST'])
@finance.route('/averageprice/', methods = ['GET', 'POST'])
def render_averageprice():
    """
        Renders the averageprice page.
    """
    # TODO: testing and correcting
    l_form = FormAveragePrice()
    if l_form.validate_on_submit():
        # TODO: remove after testing:
        l_sharesprice1 = SharesPrice(153, 12.18) # test
        l_sharesprice2 = SharesPrice(240, 23.65) # test
        print(lcf.calculate_average_price(2, byref(l_sharesprice1), byref(l_sharesprice2))) # test
        # TODO: perhaps make this hard-coded/non-dynamic for now? Like showing 50 records.
        l_average_price = lcf.calculate_average_price(int(request.form['p_total_transactions']))
        return render_template('finance/averageprice.tpl', p_form = l_form, p_average_price = l_average_price)
    return render_template('finance/averageprice.tpl', p_form = l_form)

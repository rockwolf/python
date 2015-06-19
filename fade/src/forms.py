#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired


class FormLeveragedContracts(Form):
    """
        FormLeveragedContracts
    """
    p_contracts = IntegerField('contracts', validators=[DataRequired()], default=1)


class FormTradingJournal(Form):
    """
        FormTradingJournal
    """
    p_trade_id = IntegerField('trade_id', validators=[DataRequired()], default=1)
    # TODO: needs more fields

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
    # TODO: needs more fields

class FormAccount(Form):
    """
        FormAccount
    """
    p_account_name = StringField('name', validators=[DataRequired()])
    p_account_description = StringField('description', validators=[])
    p_account_is_active = BooleanField('is_active', validators=[])
    #p_trade_id = IntegerField('trade_id', validators=[DataRequired()], default=1)
    # TODO: needs more fields
    
class FormCommodity(Form):
    """
        FormCommodity
    """
    #p_trade_id = IntegerField('trade_id', validators=[DataRequired()], default=1)
    # TODO: needs more fields

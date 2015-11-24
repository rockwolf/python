#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""
from flask.ext.wtf import Form
from wtforms import IntegerField, StringField, BooleanField, DateTimeField, HiddenField
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
    #account_id = IntegerField('account_id', validators=[])
    account_id = HiddenField()
    name = StringField('name', validators=[])
    description = StringField('description', validators=[])
    is_active = BooleanField('is_active', validators=[])
    date_modified = DateTimeField('date_modified', validators=[])
    date_created = DateTimeField('date_created', validators=[])

class FormDrawdown(Form):
    """
        FormDrawdown
    """
    drawdown_id = HiddenField()
    drawdown_current = IntegerField('drawdown_current', validators=[DataRequired()], default=0)
    drawdown_max = IntegerField('drawdown_max', validators=[DataRequired()], default=0)
    date_modified = DateTimeField('date_modified', validators=[])
    date_created = DateTimeField('date_created', validators=[])

class FormCommodity(Form):
    """
        FormCommodity
    """
    #p_trade_id = IntegerField('trade_id', validators=[DataRequired()], default=1)
    # TODO: needs more fields

class FormTest(Form):
    """
        FormAccount
    """
    account_id = HiddenField()
    name = StringField('name', validators=[])
    description = StringField('description', validators=[])
    is_active = BooleanField('is_active', validators=[])
    date_modified = DateTimeField('date_modified', validators=[])
    date_created = DateTimeField('date_created', validators=[])

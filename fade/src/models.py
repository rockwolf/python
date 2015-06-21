#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""

from src import db

class T_FINANCE(db.Model):
    """ T_FINANCE """
    #__tablename__ = Table.FINANCE
    #__table_args__ = {'autoload':True}
    #NOTE: autoload gives less control and I don't know
    #how to make session.add_all() to work with it.
    finance_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    account_from_id = db.Column(db.Integer)
    account_to_id = db.Column(db.Integer)
    amount = db.Column(db.Numeric(18, 6))
    comment = db.Column(db.String(256))
    currency_exchange_id = db.Column(db.Integer)
    rate_id = db.Column(db.Integer)
    active = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)

    def __init__(self, finance_id, date, year, month, day, account_from_id,
            account_to_id, amount, comment, currency_exchange_id,
            rate_id, active, date_created, date_modified):
        self.finance_id = finance_id
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.account_from_id = account_from_id
        self.account_to_id = account_to_id
        self.amount = amount
        self.comment = comment
        self.currency_exchange_id = currency_exchange_id
        self.rate_id = rate_id
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day,
            self.account_from_id, self.account_to_id, self.amount,
            self.comment, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)



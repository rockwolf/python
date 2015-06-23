#!/usr/bin/env python
"""
    See LICENSE.txt file for copyright and license details.
"""

from src import db

class T_ACCOUNT(db.Model):
    """
        T_ACCOUNT
    """
    account_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(4000), nullable=False, default='')
    description = db.Column(db.String(4000), nullable=False, default='')
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    date_modified = db.Column(db.DateTime, nullable=False, default='1900-01-01')

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.account_id, self.name, self.description,
            self.active, self.date_created, self.date_modified)

 
class T_FINANCE(db.Model):
    """
        T_FINANCE
    """
    #__tablename__ = Table.FINANCE
    #__table_args__ = {'autoload':True}
    #NOTE: autoload gives less control and I don't know
    #how to make session.add_all() to work with it.
    finance_id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    year = db.Column(db.Integer, nullable=False, default=1)
    month = db.Column(db.Integer, nullable=False, default=1)
    day = db.Column(db.Integer, nullable=False, default=1)
    account_from_id = db.Column(db.Integer, db.ForeignKey("T_ACCOUNT.account_id"), nullable=False, default=-1)
    account_to_id = db.Column(db.Integer, db.ForeignKey("T_ACCOUNT.account_id"), nullable=False, default=-1)
    amount = db.Column(db.Numeric(18, 6), nullable=False, default=0.0)
    comment = db.Column(db.String(256), nullable=False, default='')
    currency_exchange_id = db.Column(db.Integer, , db.ForeignKey("T_CURRENCY_EXCHANGE.currency_exchange_id"), nullable=False, default=-1)
    rate_id = db.Column(db.Integer, db.ForeignKey("T_RATE.rate_id"), nullable=False, default=-1)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    date_modified = db.Column(db.DateTime, nullable=False, default='1900-01-01')

    def __repr__(self):
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day,
            self.account_from_id, self.account_to_id, self.amount,
            self.comment, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)


class T_TRADE(db.Model):
    """
        T_TRADE
    """
    #__tablename__ = Table.TRADE
    #__table_args__ = {'autoload':True}
    #NOTE: autoload gives less control and I don't know
    #how to make session.add_all() to work with it.
    trade_id = db.Column(db.Integer, primary_key=True, nullable=False)
    trade_calculated_id = db.Column(db.Integer, db.ForeignKey("T_TRADE_CALCULATED.trade_calculated_id"), nullable=False, default=-1)
    market_id = db.Column(db.Integer, db.ForeignKey("T_MARKET.market_id"), nullable=False)
    commodity_id = db.Column(db.Integer, db.ForeignKey("T_COMMODITY.commodity_id"), nullable=False)
    date_buy = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    year_buy = db.Column(db.Integer, nullable=False, default=1)
    month_buy = db.Column(db.Integer, nullable=False, default=1)
    day_buy = db.Column(db.Integer, nullable=False, default=1)
    date_sell = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    year_sell = db.Column(db.Integer, nullable=False, default=1)
    month_sell = db.Column(db.Integer, nullable=False, default=1)
    day_sell = db.Column(db.Integer, nullable=False, default=1)
    is_long = db.Column(db.Boolean, nullable=False, default=False) 
    price_buy_orig = db.Column(db.Numeric(18, 6), nullable=False, default=0.0)
    price_sell_orig = db.Column(db.Numeric(18, 6), nullable=False, default=0.0)
    shares_buy = db.Column(db.Integer, nullable=False, default=0)
    shares_sell = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(256), nullable=False, default='')
    currency_exchange_id_buy = db.Column(db.Integer, db.ForeignKey("T_CURRENCY_EXCHANGE.currency_exchange_id"), nullable=False, default=-1)
    currency_exchange_id_sell = db.Column(db.Integer, db.ForeignKey("T_CURRENCY_EXCHANGE.currency_exchange_id"), nullable=False, default=-1)
    rate_id_buy = db.Column(db.Integer, db.ForeignKey("T_RATE.rate_id"), nullable=False, default=-1)
    rate_id_sell = db.Column(db.Integer, db.ForeignKey("T_RATE.rate_id"), nullable=False, default=-1)
    risk_input_percent = db.Column(db.Numeric(18, 6), nullable=False, default=0.0)
    is_winner = db.Column(db.Boolean, nullable=False, default=False) 
    drawdown_id = db.Column(db.Integer, db.ForeignKey("T_DRAWDOWN.drawdown_id"), nullable=False, default=-1)
    trade_pool_id = db.Column(db.Integer, db.ForeignKey("T_TRADE_POOL.trade_pool_id"), nullable=False, default=-1)
    date_expiration = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    is_expired = db.Column(db.Boolean, nullable=False, default=False) 
    is_active = db.Column(db.Boolean, nullable=False, default=False) 
    is_reconciled = db.Column(db.Boolean, nullable=False, default=False) 
    date_created = db.Column(db.DateTime, nullable=False, default='1900-01-01')
    date_modified = db.Column(db.DateTime, nullable=False, default='1900-01-01')

    def __repr__(self):
        return "<T_TRADE('%s', '%s', '%s', '%s', '%s')>" % (
            self.trade_id, self.date_buy, self.date_sell, self.date_created, self.date_modified)



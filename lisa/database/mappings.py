#! /usr/local/bin/python
"""
This file is part of Lisa.

Clipf2db is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
					
"""
class T_FINANCE(object):
    """ T_FINANCE """

    def __init__(self, date, account_id, category_id, subcategory_id,
            amount, comment, stock,
            market, shares, price, tax, commission, active, date_created,
            date_modified, risk, year, month, day):
        self.date = date
        self.account_id = account_id
        self.category_id = category_id 
        self.subcategory_id = subcategory_id 
        self.amount = amount
        self.comment = comment
        self.stock = stock
        self.market = market
        self.shares = shares
        self.price = price
        self.tax = tax
        self.commission = commission
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified
        self.risk = risk
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.date, self.account_id, self.category_id, self.subcategory_id, 
            self.amount, self.comment, self.stock, self.market, self.shares, 
            self.price, self.tax, self.commission, self.active, self.date_created,
            self.date_modified, self.risk, self.year, self.month, self.day)

class T_STOCK(object):
    """ T_STOCK """

    def __init__(self, finance_id, stock_name_id, action, price, shares, tax, commission, historical, date_created, date_modified, risk):
        self.finance_id = finance_id
        self.stock_name_id = stock_name_id
        self.action = action
        self.price = price
        self.shares = shares
        self.tax = tax
        self.commission = commission
        self.historical = historical
        self.date_created = date_created
        self.date_modified = date_modified
        self.risk = risk

    def __repr__(self):
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.finance_id, self.stock_name_id, self.action, self.price, self.shares, self.tax, self.commission, self.historical, self.date_created, self.date_modified, self.risk)

class T_STOCK_CURRENT(object):
    """ T_STOCK_CURRENT"""

    def __init__(self, code, name, shares, current_value, buy_value, amount, historical, yield_, yield_percent, date_created, date_modified):
        self.code = code
        self.name = name
        self.shares = shares
        self.current_value = current_value
        self.buy_value = buy_value
        self.amount = amount
        self.historical = historical
        self.yield_ = yield_percent
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_STOCK_CURRENT('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.code, self.name, self.shares, self.current_value, self.buy_value, self. amount, self.historical, self.yield_, self.yield_percent, self.date_created, self.date_modified)


class T_STOCK_NAME(object):
    """ T_STOCK_NAME """

    def __init__(self, name, market_id, description, date_created, date_modified):
        self.name = name
        self.market_id = market_id
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_STOCK_NAME('%s', '%s', '%s', '%s', '%s')>" % (self.name, self.market_id, self.description, self.date_created, self.date_modified)

class T_MARKET(object):
    """ T_MARKET """

    def __init__(self, code, name, country, date_created, date_modified):
        self.code = code
        self.name = name
        self.country = country
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARKET('%s', '%s', '%s', '%s', '%s')>" % (self.code, self.name, self.country, self.date_created, self.date_modified)

class T_CATEGORY(object):
    """ T_CATEGORY """

    def __init__(self, subcategory_id, name, flg_income, date_created, date_modified):
        self.subcategory_id = subcategory_id
        self.name = name
        self.flg_income = flg_income 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CATEGORY('%s', '%s', '%s', '%s', '%s')>" % (self.subcategory_id, self.name, self.flg_income, self.date_created, self.date_modified)

class T_MARGIN(object):
    """ T_MARGIN """

    def __init__(self, margin_id, margin_type_id, description, value, date_created, date_modified):
        self.margin_id = margin_id
        self.margin_type_id = margin_type_id
        self.description = description 
        self.value = value 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARGIN('%s', '%s', '%s', '%s' ,'%s', '%s')>" % (self.margin_id, self.margin_type_id, 
                self.description, self.value, self.date_created, self.date_modified)

class T_MARGIN_TYPE(object):
    """ T_MARGIN_TYPE """

    def __init__(self, margin_type_id, margin_type):
        self.margin_type_id = margin_type_id
        self.margin_type = margin_type

    def __repr__(self):
        return "<T_MARGIN_TYPE('%s', '%s')>" % (self.margin_type_id, self.margin_type)

class T_SUBCATEGORY(object):
    """ T_SUBCATEGORY """

    def __init__(self, name, date_created, date_modified):
        self.name = name
        self.date_created = date_created 
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_SUBCATEGORY('%s', '%s', '%s')>" % (self.name, self.date_created, self.date_modified)

class T_ACCOUNT(object):
    """ T_ACCOUNT """

    def __init__(self, name, date_created, date_modified):
        self.name = name
        self.date_created = date_created 
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_ACCOUNT('%s', '%s', '%s')>" % (self.name, self.date_created, self.date_modified)

class T_CURRENCY(object):
    """ T_CURRENCY """

    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __repr__(self):
        return "<T_CURRENCY('%s', '%s')>" % (self.code, self.description)

class T_CURRENCY_EXCHANGE(object):
    """ T_CURRENCY_EXCHANGE """

    def __init__(self, currency_id, exchange_rate, finance_id):
        self.currency_id = currency_id 
        self.exchange_rate = exchange_rate
        self.finance_id = finance_id

    def __repr__(self):
        return "<T_CURRENCY_EXCHANGE('%s', '%s', '%s')>" % (self.currency_id,
                self.exchange_rate, self.finance_id)

class T_FORMULA(object):
    """ T_FORMULA """

    def __init__(self, formula_id, value, description):
        self.formula_id = formula_id 
        self.value = value 
        self.description = description

    def __repr__(self):
        return "<T_FORMULA('%s', '%s', '%s')>" % (self.formula_id,
                self.value, self.description)

class T_TRADE(object):
    """ T_TRADE """
    #TODO: accuracy? Isn't that displayed with the R_multiple? Look this up!
    #TODO: drawdown: needs an input... perhaps leave this out and use a max of
    #2 days always?

    def __init__(self, trade_id, stock_id, date_buy, year_buy, month_buy,
            day_buy, date_sell, year_sell, month_sell, day_sell, long_flag,
            buy_price, sell_price, risk, initial_risk, initial_risk_percent,
            stoploss, profit_loss, profit_loss_percent, r_multiple,
            win_flag, at_work, accuracy, drawdown, id_buy, id_sell,
            currency_id, date_created, date_modified):
        self.formula_id = formula_id 
        self.value = value 
        self.description = description

    def __repr__(self):
        return "<T_CURRENCY_EXCHANGE('%s', '%s', '%s')>" % (self.formula_id,
                self.value, self.description)


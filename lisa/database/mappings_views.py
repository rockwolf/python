#! /usr/local/bin/python
"""
This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
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
class V_FINANCE(object):
    """ V_FINANCE """

    def __init__(self, finance_id, date, year, month, day, account_id, category_id,
            subcategory_id, amount, comment, stock_name_id, shares, price, tax,
            commission, active, rate_id, currency_exchange_id, date_created, date_modified):
        self.finance_id = finance_id
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.account_id = account_id
        self.category_id = category_id 
        self.subcategory_id = subcategory_id 
        self.amount = amount
        self.comment = comment
        self.stock_name_id = stock_name_id
        self.shares = shares
        self.price = price
        self.tax = tax
        self.commission = commission
        self.active = active
        self.rate_id = rate_id 
        self.currency_exchange_id = currency_exchange_id
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
            '%s')>" % (
            self.finance_id, self.date, self.year, self.month, self.day, self.account_id,
            self.category_id, self.subcategory_id, self.amount, self.comment,
            self.stock_name_id, self.shares, self.price, self.tax,
            self.commission, self.active, self.rate_id,
            self.currency_exchange_id, self.date_created, self.date_modified)

class V_INVESTMENT(object):
    """ V_INVESTMENT """

    def __init__(self, investment_id, stock_name_id, action, price, shares, tax,
            commission, historical, active, date_created, date_modified, risk):
        self.investment_id = investment_id
        self.stock_name_id = stock_name_id
        self.action = action
        self.price = price
        self.shares = shares
        self.tax = tax
        self.commission = commission
        self.historical = historical
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified
        self.risk = risk

    def __repr__(self):
        return "<V_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.investment_id, self.stock_name_id, self.action, self.price, self.shares, self.tax, self.commission, self.historical, self.active, self.date_created, self.date_modified, self.risk)

class V_STOCK_NAME(object):
    """ V_STOCK_NAME """

    def __init__(self, stock_name_id, name, market_id, description, date_created, date_modified):
        self.stock_name_id = stock_name_id
        self.name = name
        self.market_id = market_id
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_STOCK_NAME('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.stock_name_id, self.name, 
                self.market_id, self.description, self.date_created, self.date_modified)

class V_MARKET(object):
    """ V_MARKET """

    def __init__(self, market_id, code, name, country, active, date_created, date_modified):
        self.market_id = market_id
        self.code = code
        self.name = name
        self.country = country
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_MARKET('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.market_id, self.code, self.name, self.country, self.active, self.date_created, self.date_modified)

class V_CATEGORY(object):
    """ V_CATEGORY """

    def __init__(self, subcategory_id, name, flg_income, active, date_created, date_modified):
        self.subcategory_id = subcategory_id
        self.name = name
        self.flg_income = flg_income 
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_CATEGORY('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.subcategory_id, 
                self.name, self.flg_income, self.active, self.date_created, self.date_modified)

class V_MARGIN(object):
    """ V_MARGIN """

    def __init__(self, margin_id, margin_type_id, description, value, date_created, date_modified):
        self.margin_id = margin_id
        self.margin_type_id = margin_type_id
        self.description = description 
        self.value = value 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_MARGIN('%s', '%s', '%s', '%s' ,'%s', '%s')>" % (self.margin_id, self.margin_type_id, 
                self.description, self.value, self.date_created, self.date_modified)

class V_MARGIN_TYPE(object):
    """ V_MARGIN_TYPE """

    def __init__(self, margin_type_id, margin_type):
        self.margin_type_id = margin_type_id
        self.margin_type = margin_type

    def __repr__(self):
        return "<V_MARGIN_TYPE('%s', '%s')>" % (self.margin_type_id, self.margin_type)

class V_SUBCATEGORY(object):
    """ V_SUBCATEGORY """

    def __init__(self, subcategory_id, name, active, date_created, date_modified):
        self.subcategory_id = subcategory_id
        self.name = name
        self.active = active
        self.date_created = date_created 
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_SUBCATEGORY('%s', '%s', '%s', '%s', '%s')>" % (self.subcategory_id, self.name,
                self.active, self.date_created, self.date_modified)

class V_ACCOUNT(object):
    """ V_ACCOUNT """

    def __init__(self, account_id, name, description, active, date_created, date_modified):
        self.account_id = account_id
        self.name = name
        self.description = description
        self.active = active
        self.date_created = date_created 
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_ACCOUNT('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.account_id, self.name, 
                self.description, self.active, self.date_created, self.date_modified)

class V_CURRENCY(object):
    """ V_CURRENCY """

    def __init__(self, currency_id, code, description):
        self.currency_id = currency_id
        self.code = code
        self.description = description

    def __repr__(self):
        return "<V_CURRENCY('%s', '%s', '%s')>" % (self.currency_id, self.code, self.description)

class V_CURRENCY_EXCHANGE(object):
    """ V_CURRENCY_EXCHANGE """

    def __init__(self, currency_exchange_id, currency_id, exchange_rate,
            date_created, date_modified):
        self.currency_exchange_id = currency_exchange_id
        self.currency_id = currency_id 
        self.exchange_rate = exchange_rate
        self.date_created = date_created 
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_CURRENCY_EXCHANGE('%s', '%s', '%s', '%s', '%s')>" % (self.currency_exchange_id, self.currency_id,
                self.exchange_rate, self.date_created, self.date_modified)

class V_FORMULA(object):
    """ V_FORMULA """

    def __init__(self, formula_id, value, description):
        self.formula_id = formula_id 
        self.value = value 
        self.description = description

    def __repr__(self):
        return "<V_FORMULA('%s', '%s', '%s')>" % (self.formula_id,
                self.value, self.description)

class V_TRADE(object):
    """ V_TRADE """
    #TODO: accuracy? Isn't that displayed with the R_multiple? Look this up!
    #TODO: drawdown: needs an input... perhaps leave this out and use a max of
    #2 days always?

    def __init__(self, trade_id, date_buy, year_buy, month_buy,
            day_buy, date_sell, year_sell, month_sell, day_sell, long_flag,
            price_buy, price_sell, risk, initial_risk, initial_risk_percent,
            stoploss, profit_loss, profit_loss_percent, r_multiple,
            win_flag, at_work, id_buy, id_sell,
            currency_id, drawdown_id, active, date_created, date_modified):
        self.trade_id = trade_id 
        self.date_buy = date_buy
        self.year_buy = year_buy
        self.month_buy = month_buy
        self.day_buy = day_buy
        self.date_sell = date_sell
        self.year_sell = year_sell
        self.month_sell = month_sell
        self.day_sell = day_sell
        self.long_flag = long_flag
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.risk = risk
        self.initial_risk = initial_risk
        self.initial_risk_percent = initial_risk_percent
        self.stop_loss = stoploss
        self.profit_loss = profit_loss
        self.profit_loss_percent = profit_loss_percent
        self.r_multiple = r_multiple
        self.win_flag = win_flag
        self.at_work = at_work
        self.id_buy = id_buy
        self.id_sell = id_sell
        self.currency_id = currency_id
        self.active = active
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_TRADE('%s', '%s', '%s', '%s', '%s', '%s', \
                '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
                '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
                '%s', '%s', '%s', '%s', '%s')>" % (self.trade_id, 
                        self.date_buy,
                        self.year_buy,
                        self.month_buy,
                        self.day_buy,
                        self.date_sell,
                        self.year_sell,
                        self.month_sell,
                        self.day_sell,
                        self.long_flag,
                        self.price_buy,
                        self.price_sell,
                        self.risk,
                        self.initial_risk,
                        self.initial_risk_percent,
                        self.stoploss,
                        self.profit_loss,
                        self.profit_loss_percent,
                        self.r_multiple,
                        self.win_flag,
                        self.at_work,
                        self.id_buy,
                        self.id_sell,
                        self.currency_id,
                        self.drawdown_id,
                        self.active,
                        self.date_created,
                        self.date_modified)

class V_RATE(object):
    """ V_RATE """

    def __init__(self, rate_id, calculated, calculated_percent,
            on_shares, on_commission, on_ordersize, on_other, commission, tax,
            formula_id, manual_flag, date_created, date_modified):
        self.rate_id = rate_id
        self.calculated = calculated
        self.calculated_percent = calculated_percent
        self.on_shares = on_shares
        self.on_commission = on_commission
        self.on_ordersize = on_ordersize
        self.on_other = on_other
        self.commission = commission
        self.tax = tax
        self.formula_id = formula_id
        self.manual_flag = manual_flag
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_RATE('%s', '%s', '%s', '%s', '%s', '%s', '%s', \
                '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.rate_id,
                        self.calculated, self.calculated_percent, self.on_shares,
                        self.on_commission, self.on_ordersize, self.on_other,
                        self.commission, self.tax, self.formula_id,
                        self.manual_flag, self.date_created, self.date_modified)

class V_DRAWDOWN(object):
    """ V_DRAWDOWN """

    def __init__(self, drawdown_id, value, date_created, date_modified):
        self.drawdown_id = drawdown_id 
        self.value = value 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<V_DRAWDOWN('%s', '%s', '%s', '%s')>" % (self.drawdown_id,
                self.value, self.date_created, self.date_modified)

class V_PARAMETER(object):
    """ V_PARAMETER """

    def __init__(self, parameter_id, name, value, description):
        self.parameter_id = parameter_id
        self.name = name
        self.value = value 
        self.description = description

    def __repr__(self):
        return "<V_PARAMETER('%s', '%s', '%s', '%s')>" % (self.parameter_id, self.name,
                self.value, self.description)

class V_REP_CHECK_TOTAL(object):
    """ V_REP_CHECK_TOTAL """

    def __init__(self, account_name, account_total):
        self.account_name = account_name
        self.account_total = account_total

    def __repr__(self):
        return "<V_REP_CHECK_TOTAL('%s', '%s')>" % (self.account_name,
                self.account_total)
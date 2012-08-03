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

    def __init__(self, date, aid, cid, amount, comment, stock, market, shares, price, tax, commission, active, date_created, date_modified, risk, year, month, day):
        self.date = date
        self.aid = aid
        self.cid = cid 
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
        return "<T_FINANCE('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
    '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" %
    (self.date, self.aid, self.cid, self.amount, self.comment,
            self.stock, self.market, self.shares, self.price, self.tax,
            self.commission, self.active, self.date_created,
            self.date_modified, self.risk, self.year, self.month, self.day)

class T_STOCK(object):
    """ T_STOCK """

    def __init__(self, id, snid, action, price, shares, tax, commission, historical, date_created, date_modified, risk):
        self.id = id
        self.snid = snid
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
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.snid, self.action, self.price, self.shares, self.tax, self.commission, self.historical, self.date_created, self.date_modified, self.risk)

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

    def __init__(self, name, mid, description, date_created, date_modified):
        self.name = name
        self.mid = mid
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_STOCK_NAME('%s', '%s', '%s', '%s', '%s')>" % (self.name, self.mid, self.description, self.date_created, self.date_modified)

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

    def __init__(self, scid, name, flg_income, date_created, date_modified):
        self.scid = scid
        self.name = name
        self.flg_income = flg_income 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_CATEGORY('%s', '%s', '%s', '%s', '%s')>" % (self.scid, self.name, self.flg_income, self.date_created, self.date_modified)

class T_MARGIN(object):
    """ T_MARGIN """

    def __init__(self, smid, margin_type_id, description, value, date_created, date_modified):
        self.smid = smid
        self.margin_type_id = margin_type_id
        self.description = description 
        self.value = value 
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_MARGIN('%s', '%s', '%s', '%s' ,'%s', '%s')>" % (self.smid, self.margin_type_id, self.description, value, self.date_created, self.date_modified)

class T_MARGIN_TYPE(object):
    """ T_MARGIN_TYPE """

    def __init__(self, mtid, margin_type):
        self.mtid = mtid
        self.margin_type = margin_type

    def __repr__(self):
        return "<T_MARGIN_TYPE('%s', '%s')>" % (self.mtid, self.margin_type)

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

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

class T_STOCK(object):
    """ T_STOCK """

    def __init__(self, id, snid, action, price, quantity, historical, date_create, date_modify):
        self.id = id
        self.snid = snid
        sef.action = action
        self.price = price
        self.quantity = quantity
        self.historical = historical
        self.date_create = date_create
        self.date_modify = date_modify

    def __repr__(self):
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.snid, self.action, self.price, self.quantity, self.historical, self.date_create, self.date_modify)

class T_STOCK_NAME(object):
    """ T_STOCK_NAME """

    def __init__(self, snid, name, mid, description, date_create, date_modify):
        self.snid = snid
        self.name = name
        self.mid = mid
        self.description = description
        self.date_create = date_create
        self.date_modify = date_modify

    def __repr__(self):
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.snid, self.name, self.mid, self.description, self.date_create, self.date_modify)

class T_MARKET(object):
    """ T_MARKET """

    def __init__(self, mid, code, name, date_create, date_modify):
        self.mid = mid
        self.code = code
        self.name = name
        self.date_create = date_create
        self.date_modify = date_modify

    def __repr__(self):
        return "<T_MARKET('%s', '%s', '%s', '%s', '%s')>" % (self.mid, self.code, self.name, self.date_create, self.date_modify)

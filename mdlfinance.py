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

class T_FINANCE(object):
    """ T_STOCK """

    def __init__(self, id, date, account, product, oid, amount, flag, comment, tags, date_create, date_modify):
        self.id = id
        self.date = date
        self.account = account
        self.product = product,
        self.oid = oid
        self.amount = amount
        self.flag = flag
        self.comment = comment
        self.tags = tags
        self.date_create = date_create
        self.date_modify = date_modify

    def __repr__(self):
        return "<T_STOCK('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.id, self.date, self.account, self.product, self.oid, self.amount, self.flag, self.comment, self.tags,  self.date_create, self.date_modify)

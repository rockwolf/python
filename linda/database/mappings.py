#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.constant import *
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from meta import Base

class T_DRAWDOWN(Base):
    """ T_DRAWDOWN """
    __tablename__ = TABLE_DRAWDOWN
    #__table_args__ = {'autoload':True}
    drawdown_id = Column(Integer, primary_key=True)
    drawdown_current = Column(Integer)
    drawdown_max = Column(Integer)
    date_created = Column(DateTime)
    date_modified = Column(DateTime)

    def __init__(self, drawdown_id, drawdown_current, drawdown_max,
            date_created,date_modified):
        self.drawdown_id = drawdown_id
        self.drawdown_current = drawdown_current
        self.drawdown_max = drawdown_max
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<T_DRAWDOWN('%s', '%s', '%s', '%s', '%s')>" % (
                self.drawdown_id,
                self.drawdown_current,
                self.drawdown_max,
                self.date_created,
                self.date_modified)

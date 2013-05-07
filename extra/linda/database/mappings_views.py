#!/usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.constant import *
from sqlalchemy import Column, Integer, String
from meta import Base

class V_DRAWDOWN(Base):
    """ V_DRAWDOWN """
    __tablename__ = VIEW_DRAWDOWN
    __table_args__ = {'autoload':True}
    drawdown_id = Column('drawdown_id', Integer, primary_key=True)

#TODO: create view for V_DRAWDOWN_ACTIVE
# in sql and in this mapping, for display of active trades in the
# table view. This info will have to contain the drawdown_id, so we can
# update TABLE_DRAWDOWN from mappings.py

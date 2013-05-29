#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.	
"""

from decimal import Decimal
from enum import Enum

DEFAULT_DECIMAL = Decimal(0.0)

class Transaction(Enum):
    BUY = 0
    SELL = 1

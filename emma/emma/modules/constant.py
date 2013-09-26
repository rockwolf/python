#!/usr/local/bin/python
"""
    See LICENSE file for copyright and license details.	
"""

from decimal import Decimal

DEFAULT_DECIMAL = Decimal(-1.0)
DEFAULT_CURRENCY = "USD"

class Transaction():
    BUY = 0
    SELL = 1

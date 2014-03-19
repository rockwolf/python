#! /usr/local/bin/python
"""
See LICENSE file for copyright and license details.
"""

from modules.constant import *
from modules.function import *
from generic.modules.calculator_finance import *
from decimal import Decimal
from generic.modules.function import print_in_columns

class Emma():
    """
        Emma class
    """
   
    def __init__(self, input_line):
        """
            Initialize
        """
        self.input_line = input_line
        # result
        self.result = {}
  
    def calculate(self):
        """
            Calculate all possible unknown values.
        """
        result = {}
        try:
            #Note: the order is important...
            # Input values
            buying = we_are_buying(
                self.input_line[Input.ACCOUNT_FROM],
                self.input_line[Input.ACCOUNT_TO])

            # Extra calculatable fields
            self.result["shares"] = calculate_shares_recommended(
                    self.get_pool_without_margin(self.input_line[Input.POOL]), self.dba.get_margin_pool()
                    , buying)
        except Exception as ex:
            print 'Error in calculate:', ex

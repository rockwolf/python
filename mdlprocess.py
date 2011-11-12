#! /usr/local/bin/python
"""
This file is part of Emma.

Emma is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Emma is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Emma. If not, see <http://www.gnu.org/licenses/>.
					
"""
from decimal import Decimal

class Process():
    """ Class that contains values from the config file. """

    def __init__(self, config):
        """ Initialise class. """ 
        self.config = config
        self.capital = 30000
        self.use = 2000
        self.price = 12
        self.tax = Decimal(self.config.tax)/100
        self.commission = 7.25
 
    def buy(self):
        """ Process buy values. """
        shares = 0
        self.output_header()
        self.output_buy()
        self.output_sell()
        self.output_general()

    def output_header(self):
        """ Header portion of the output. """
        header = 'C: ' + str(self.capital) + ' | u: ' + str(self.use) + \
                ' | p: ' + str(self.price) + ' | t: ' + str(self.tax) + \
                ' | c: ' + str(self.commission)
        print(header)
        print('-'*len(header))
        
    def output_buy(self):
        """ Buy portion of the output. """
        print('BUY\n---')
        
    def output_sell(self):
        """ Sell portion of the output. """
        print('SELL\n---')

    def output_general(self):
        """ General portion of the output. """
        print('TOTAL\n-----');

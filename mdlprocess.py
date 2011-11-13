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
from decimal import *

class Process():
    """ Class that contains values from the config file. """

    def __init__(self, config, capital, used, \
            tax, commission, price, risk, \
            sellprice, amount, verbose):
        """ Initialise class. """ 
        # input
        self.config = config
        self.capital = capital
        self.used = used
        self.tax = tax
        self.commission = commission
        self.price = price
        self.risk = risk
        # calculated
        self.buy_shares = 0
        self.buy_stoploss = 0.0
        self.buy_lossontax = 0.0
        self.buy_lossoncommission = 0.0
        self.buy_losstotal = 0.0
        self.sell_return = 0.0
        self.sell_profit = 0.0
        self.sell_lossontax = 0.0
        self.sell_lossoncommission = 0.0
        self.sell_losstotal = 0.0
        self.total_stillinvested = 0.0
        self.total_sharesleft = 0
        self.total_lossontax = 0.0
        self.total_lossoncommission = 0.0
        self.total_losstotal = 0.0
 
    def buy(self,):
        """ Process buy values. """
        shares = 0
        self.output_header()
        self.output_buy()
        self.output_sell()
        self.output_general()

    def output_header(self):
        """ Header portion of the output. """
        getcontext().prec = 2
        header = 'C: ' + str(self.capital) + ' | u: ' + str(self.used) + \
                ' | p: ' + str(self.price) + ' | t: ' + str(self.tax*100) + '%'\
                ' | c: ' + str(self.commission) + ' | r: ' + str(self.risk*100) + '%'
        print(header)
        print('-'*len(header))
        
    def output_buy(self):
        """ Buy portion of the output. """
        print('\nBUY\n---')
        print('Shares to buy: ', self.buy_shares)
        print('Stop loss: ', self.buy_stoploss)
        print('Loss on tax: ', self.buy_lossontax)
        print('Loss on commission: ', self.buy_lossoncommission)
        print('Loss total: ', self.buy_losstotal)
        
    def output_sell(self):
        """ Sell portion of the output. """
        print('\nSELL\n----')
        print('Return: ', self.sell_return)
        print('Profit: ', self.sell_profit)
        print('Loss on tax: ', self.sell_lossontax)
        print('Loss on commission: ', self.sell_lossoncommission)
        print('Loss total: ', self.sell_losstotal)

    def output_general(self):
        """ General portion of the output. """
        print('\nTOTAL\n-----');
        print('Money still invested: ', self.total_stillinvested)
        print('Shares left: ', self.total_sharesleft)
        print('Loss on tax: ', self.total_lossontax)
        print('Loss on commission: ', self.total_lossoncommission)
        print('Loss total: ', self.total_losstotal)

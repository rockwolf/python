#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.function import *

class Rate(CoreModule):
    """
        Rate class.
    """

    def create_statements(self, input_fields):
        """
            Creates the records needed for TABLE_RATE
            and returns them as a Statement object.
        """
        try:
            date_created = current_date()
            date_modified = current_date()
            statement_rate = Statement(TABLE_RATE)
            records = 0
            for fields in input_fields:
                if deals_with_stocks(fields['category'], fields['subcategory']):
                    formula_id = self.get_formula_id_to_use(fields)
                    records = records + 1
                    
                    if fields['manual_flag'] == 1:
                        commission = fields['commission']
                        tax = fields['tax']
                        on_shares = DEFAULT_DECIMAL
                        on_commission = DEFAULT_DECIMAL 
                        on_ordersize = DEFAULT_DECIMAL
                        on_other = DEFAULT_DECIMAL
                        calculated = DEFAULT_DECIMAL
                    else:
                        #TODO: calculate something when necessary
                        on_shares = DEFAULT_DECIMAL
                        #TODO: calculate something when necessary
                        on_commission = DEFAULT_DECIMAL
                        trade_id = trade_record['trade_id']
                        #TODO: calculate something when necessary
                        on_ordersize = DEFAULT_DECIMAL
                        #TODO: actually calculate something when necessary
                        on_other = DEFAULT_DECIMAL
                        #TODO: these functions need to come from another place,
                        #so we can call them here.
                        calculated = self.calculate_commission()
                        commission = self.get_parameter_value(
                                self.get_parameter_commission(
                                    fields['amount'], fields['market_name']))
                        tax = self.get_parameter_value(
                                self.get_parameter_tax(
                                fields['amount'], fields['market_name']))
                    
                    statement_rate.add(
                        records,
                        {
                            'rate_id':None,
                            'calculated':Decimal(calculated),
                            'calculated_percent':Decimal(calculated)/Decimal(100.0),
                            'on_shares':Decimal(on_shares),
                            'on_commission':Decimal(on_commission),
                            'on_ordersize':Decimal(on_ordersize),
                            'on_other':Decimal(on_other),
                            'commission':Decimal(commission),
                            'tax':Decimal(tax),
                            'formula_id':int(formula_id),
                            'manual_flag':int(fields['manual_flag']),
                            'date_created':date_created,
                            'date_modified':date_modified
                        }
                    )
            return statement_rate
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_RATE, ex)

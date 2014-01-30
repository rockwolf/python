#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.core_module import CoreModule
from modules.statement import Statement
from modules.constant import *
from modules.function import *
from generic.modules.function import *

class Rate(CoreModule):
    """
        Rate class.
    """

    def __init__(self, config):
        """
            Initialisation
        """
        self.config = config

    def create_statements(self, input_fields):
        """
            Creates the records needed for Table.RATE
            and returns them as a Statement object.
        """
        try:
            dba = DatabaseAccess(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_rate = Statement(Table.RATE)
            records = 0
            for fields in input_fields:
                if deals_with_commodities(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                    formula_id = dba.get_formula_id_to_use(fields)
                    records = records + 1
                    
                    if fields[Input.MANUAL_FLAG] == 1:
                        commission = fields[Input.COMMISSION]
                        tax = fields[Input.TAX]
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
                        #TODO: calculate something when necessary
                        on_ordersize = DEFAULT_DECIMAL
                        #TODO: actually calculate something when necessary
                        on_other = DEFAULT_DECIMAL
                        #TODO: these functions need to come from another place,
                        #so we can call them here.
                        calculated = dba.calculate_commission()
                        commission = dba.get_parameter_value(
                                dba.get_parameter_commission(
                                    fields[Input.AMOUNT], fields[Input.MARKET_CODE]))
                        tax = dba.get_parameter_value(
                                dba.get_parameter_tax(
                                fields[Input.AMOUNT], fields[Input.MARKET_CODE]))
                    
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
                            'manual_flag':int(fields[Input.MANUAL_FLAG]),
                            'date_created':date_created,
                            'date_modified':date_modified
                        }
                    )
            return statement_rate
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_RATE, ex
        finally:
            dba = None

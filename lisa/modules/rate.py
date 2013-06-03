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
from modules_generic.function import *

class Rate(CoreModule):
    """
        Rate class.
    """

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
                if deals_with_stocks(fields['i_category'], fields['i_subcategory']):
                    formula_id = dba.get_formula_id_to_use(fields)
                    records = records + 1
                    
                    if fields['i_manual_flag'] == 1:
                        commission = fields['i_commission']
                        tax = fields['i_tax']
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
                                    fields['i_amount'], fields['i_market_name']))
                        tax = dba.get_parameter_value(
                                dba.get_parameter_tax(
                                fields['i_amount'], fields['i_market_name']))
                    
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
                            'manual_flag':int(fields['i_manual_flag']),
                            'date_created':date_created,
                            'date_modified':date_modified
                        }
                    )
            return statement_rate
        except Exception as ex:
            print(Error.CREATE_STATEMENTS_TABLE_RATE, ex)
        finally:
            dba = None

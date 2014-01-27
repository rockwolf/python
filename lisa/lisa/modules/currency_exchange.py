#!/usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.core_module import CoreModule
from modules.statement import Statement
from modules.function import *
from modules.constant import *
from generic.modules.function import *

class CurrencyExchange(CoreModule):
    """
        CurrencyExchange class.
    """

    def __init__(self, config):
        """
            Initialisation
        """
        self.config = config

    def create_statements(self, input_fields):
        """
            Creates the records needed for Table.CURRENCY_EXCHANGE.
        """
        try:
            dba = DatabaseAccess(self.config)
            print 'test2: input_fields = ', input_fields
            #TODO: The Statement call fails, it expects no arguments?
            # Is that a python27 error?
            statement_currency_exchange = Statement(Table.CURRENCY_EXCHANGE)
            print 'test2: after Statement creation'
            date_created = current_date()
            date_modified = current_date()
            records = 0
            for fields in input_fields:
                records = records + 1
                #NOTE: we don't need to query, because we always add a new
                #currency_exchange line. The same value can be used multiple
                #times, so it's not possible to query if one already exists.
                statement_currency_exchange.add(
                    records,
                    {
                        'currency_exchange_id':None,
                        'currency_from_id':dba.currency_id_from_currency(fields[Input.CURRENCY_FROM]),
                        'currency_to_id':dba.currency_id_from_currency(fields[Input.CURRENCY_TO]),
                        'exchange_rate':Decimal(fields[Input.EXCHANGE_RATE]),
                        'date_created':date_created,
                        'date_modified':date_modified
                    }
                )
            return statement_currency_exchange
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE, ex
        finally:
            dba = None

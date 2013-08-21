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

class Bet(CoreModule):
    """
    Bet class.
    """

    def create_statements(self, input_fields):
        """
        Creates the records needed for Table.BET
        and returns them as a Statement object.
        """
        try:
            dba = DatabaseAccess(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_bet = Statement(Table.BET)
            records = 0
            for fields in input_fields:
                if is_for_betting(fields['i_account_to']):
                    records = records + 1
                    
                    pool = DEFAULT_DECIMAL
                    stake = DEFAULT_DECIMAL
                    value = DEFAULT_DECIMAL
                    difference = DEFAULT_DECIMAL
                    win = DEFAULT_INTEGER
                    win_total = DEFAULT_INT
                    win_average = DEFAULT_DECIMAL
                    average = DEFAULT_DECIMAL
                    average_total = DEFAULT_DECIMAL
                    average_percent = DEFAULT_DECIMAL
                    
                    statement_bet.add(
                        records,
                        {
                            'bet_id':None
                            , 'pool':pool
                            , 'stake':stake
                            , 'value':value
                            , 'difference':difference
                            , 'win':win
                            , 'win_total':win_total
                            , 'win_percent':win_percent
                            , 'average':average
                            , 'average_total':average_total
                            , 'average_percent':average_percent
                            , 'date_created':date_created
                            , 'date_modified':date_modified
                        }
                    )
            return statement_bet
        except Exception as ex:
            print(Error.CREATE_STATEMENTS_TABLE_BET, ex)
        finally:
            dba = None

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
from database.mappings import T_TRADE
from generic.modules.calculator_finance import CalculatorFinance

class Trade(CoreModule):
    """
        Trade class.
    """

    def __init__(self, config):
        """
            Initialisation
        """
        self.config = config
        self.statement_trade = Statement(Table.TRADE)
        self.flag_insupdel = StatementType.INSERT
        self.trade_id = DEFAULT_INT
        self.market_id = DEFAULT_INT
        self.commodity_name = ''
        self.date_buy = DEFAULT_DATE
        self.year_buy = DEFAULT_INT
        self.month_buy = DEFAULT_INT
        self.day_buy = DEFAULT_INT
        self.date_sell = DEFAULT_DATE
        self.year_sell = DEFAULT_INT
        self.month_sell = DEFAULT_INT
        self.day_sell = DEFAULT_INT
        self.long_flag = DEFAULT_INT
        self.price_buy = DEFAULT_DECIMAL
        self.price_buy_orig = DEFAULT_DECIMAL
        self.price_sell = DEFAULT_DECIMAL
        self.price_sell_orig = DEFAULT_DECIMAL
        self.shares_buy = DEFAULT_DECIMAL
        self.shares_sell = DEFAULT_DECIMAL
        self.commission_buy = DEFAULT_DECIMAL
        self.commission_sell = DEFAULT_DECIMAL
        self.tax_buy = DEFAULT_DECIMAL
        self.tax_sell = DEFAULT_DECIMAL
        self.risk_input = DEFAULT_DECIMAL
        self.risk_input_percent = DEFAULT_DECIMAL
        self.risk_initial = DEFAULT_DECIMAL
        self.risk_initial_percent = DEFAULT_DECIMAL
        self.risk_actual = DEFAULT_DECIMAL
        self.risk_actual_percent = DEFAULT_DECIMAL
        self.cost_total = DEFAULT_DECIMAL
        self.cost_other = DEFAULT_DECIMAL
        self.amount_buy_simple = DEFAULT_DECIMAL
        self.amount_sell_simple = DEFAULT_DECIMAL
        self.stoploss = DEFAULT_DECIMAL
        self.stoploss_orig = DEFAULT_DECIMAL
        self.profit_loss = DEFAULT_DECIMAL
        self.profit_loss_percent = DEFAULT_DECIMAL
        self.r_multiple = DEFAULT_DECIMAL
        self.win_flag = DEFAULT_DECIMAL
        self.id_buy = DEFAULT_INT
        self.id_sell = DEFAULT_INT
        self.currency_exchange_id = DEFAULT_INT
        self.drawdown_id = DEFAULT_INT
        self.pool_at_start = DEFAULT_DECIMAL
        self.date_expiration = DEFAULT_DATE
        self.expired_flag = DEFAULT_INT
        self.active = DEFAULT_INT
        self.date_created = DEFAULT_DATE
        self.date_modified = DEFAULT_DATE
        self.trade_record = []

    def create_statements(self, input_fields, statements_finance):
        """
            Creates the records needed for Table.TRADE and returns them as a
            Statement object.
        """
        #NOTE: price_buy will be fields['i_price']
        #When we buy more, it will be overwritten!
        #Trading without adding to positions is assumed by this code!
        try:
            dba = DatabaseAccess(self.config)
            calc = CalculatorFinance()
            self.date_created = current_date()
            self.date_modified = current_date()
            records = 0
            self.finance_id = dba.first_finance_id_from_latest()
            if self.finance_id != -1:
                for fields in input_fields:
                    if deals_with_commodities(
                        fields[Input.ACCOUNT_FROM]
                        , fields[Input.ACCOUNT_TO]):
                        records = records + 1
                        # GENERAL INFO AT START
                        self.general_info_at_start(dba, calc, fields) 
                        # UPDATE/INSERT
                        if dba.invade_already_started(self.market_id,
                                self.commodity_name_id, T_TRADE):
                            self.update_info(dba, calc, fields, self.trade_record)
                        else:
                            self.insert_info(dba, calc, fields, self.trade_record)
                        # GENERAL VARIABLES THAT CAN BE CALCULATED ON THE DATA WE HAVE
                        self.general_info_at_end(fields, self.trade_record)
                        # TEST INFO
                        self.print_test_info()
                        # ADDING THE STATEMENTS
                        self.add_to_statement(records)
                    self.finance_id = self.finance_id + 1
            return self.statement_trade
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_TRADE, ex
        finally:
            calc = None
            dba = None

    def general_info_at_start(self, dba, calc, fields):
        """
            General info at the start of the trade.
        """
        try:
            self.market_id = dba.market_id_from_market(
                fields[Input.MARKET_CODE])
            self.commodity_name_id = dba.commodity_name_id_from_commodity_name(
                fields[Input.COMMODITY_NAME], self.market_id)
            self.finance_record = dba.get_finance_record(self.finance_id)
            self.trade_record = dba.get_invade_record(self.finance_id, T_TRADE)
            self.long_flag = dba.get_long_flag_value(fields[Input.ACCOUNT_FROM],
                fields[Input.ACCOUNT_TO], self.trade_record)
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_TRADE, ex

    def update_info(self, dba, calc, fields, trade_record):
        """
            Update info.
        """
        #NOTE: Correct way of updating =  Supplier.query.filter(<your stuff here, or user filter_by, or whatever is in your where clause>).update(values)
        #e.g.: session.query(Supplier).filter_by(id=2).update({"name": u"Mayowa"})
        #TABLE_TRADE.query.filter(market_name=...,commodity_name=...).update({"date_...": date_... etc.})
        try:
            self.flag_insupdel = StatementType.UPDATE
            self.trade_id = trade_record['trade_id']
            ## buy/sell related fields
            if (we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO])
                and T_TRADE.id_buy == -1):
                self.id_buy = self.finance_id
                self.id_sell = trade_record['id_sell']
                self.date_buy = self.date_created
                self.date_sell = trade_record['date_sell']
                self.price_buy = abs(fields[Input.PRICE])
                self.price_sell = abs(trade_record['price_sell'])
                self.shares_buy = fields[Input.QUANTITY]
                self.shares_sell = trade_record['shares_sell']
                self.commission_buy = fields[Input.COMMISSION]
                self.commission_sell = trade_record['commission_sell']
                self.tax_buy = fields[Input.TAX]
                self.tax_sell = trade_record['tax_sell']
            elif (not we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO])
                and T_TRADE.id_sell == -1):
                self.id_buy = trade_record['id_buy']
                self.id_sell = self.finance_id
                self.date_buy = trade_record['date_buy']
                self.date_sell = self.date_created
                self.price_buy = abs(trade_record['price_buy'])
                self.price_sell = abs(fields[Input.PRICE])
                self.shares_buy = trade_record['shares_buy']
                self.shares_sell = fields[Input.QUANTITY]
                self.commission_buy = trade_record['commission_buy']
                self.commission_sell = fields[Input.COMMISSION]
                self.tax_buy = trade_record['tax_buy']
                self.tax_sell = fields[Input.TAX]
            else:
                raise Exception(
                    "{0} already contains a sell or buy record" \
                    " and you are trying to add one like it" \
                    " again?".format(T_TRADE))
            self.stoploss = trade_record['stoploss']
            self.profit_loss = calc.calculate_profit_loss(
                trade_record['amount_sell'],
                trade_record['amount_buy'])
            self.pool_at_start = trade_record['pool_at_start']
            self.date_created = trade_record['date_created']
            self.amount_buy_simple = trade_record['amount_buy_simple']
            self.amount_sell_simple = calc.calculate_amount_simple(
                    Decimal(fields[Input.PRICE])
                    , Decimal(fields[Input.QUANTITY]))
            self.risk_input = trade_record['risk_input']
            self.risk_input_percent = trade_record['risk_input_percent']
            self.risk_initial = trade_record['risk_initial']
            self.risk_initial_percent = (risk_initial/amount_buy_simple)*Decimal(100.0)
            self.risk_actual = calc.calculate_risk_actual(
                trade_record['price_buy'],
                trade_record['shares_buy'],
                trade_record['price_sell'],
                trade_record['shares_sell'],
                trade_record['stoploss'],
                trade_record['risk_initial'])
            self.risk_actual_percent = (risk_actual/amount_buy_simple)*Decimal(100.0)
            self.cost_total = calc.calculate_cost_total(
                trade_record['tax_buy'],
                trade_record['commission_buy'],
                trade_record['tax_sell'],
                trade_record['commission_sell'])
            self.cost_other = calc.calculate_cost_other(
                    self.cost_total,
                    self.profit_loss)
            if we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                self.win_flag = dba.get_win_flag_value(
                        self.price_buy,
                        self.trade_record['price_sell'],
                        self.long_flag)
            else:
                self.win_flag = dba.get_win_flag_value(
                        trade_record['price_buy'],
                        self.price_sell,
                        self.long_flag)
            self.currency_exchange_id = trade_record['currency_exchange_id']
            self.drawdown_id = trade_record['drawdown_id']
            self.r_multiple = calc.calculate_r_multiple(
                trade_record['price_buy'],
                trade_record['price_sell'],
                trade_record['price_stoploss'])
            self.date_expiration = trade_record['date_expiration']
            #TODO: for investing, id_buy/sell is id_firstbuy and id_firstsell
            # and expiration flag should only be set at the end of the trade, when
            # the trade is closed. This means that date_buy and date_sell is not
            # enough to determine if a trade is closed or not. The total shares
            # should also be 0 when added up OR shares_buy = shares_sell.
            # So add:
            #if trade_closed: (or something like that)
            self.expired_flag = (1 if self.date_sell > self.date_expiration else 0)
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_TRADE, ex

    def insert_info(self, dba, calc, fields, trade_record):
        """
            Insert info.
        """
        try:
            self.flag_insupdel = StatementType.INSERT
            self.trade_id = None # insert: new one created automatically
            ## buy/sell related fields
            if we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                self.id_buy = self.finance_id
                self.id_sell = -1
                self.date_buy = self.date_created
                self.date_sell = string_to_date(DEFAULT_DATE)
                self.price_buy = calc.convert_from_orig(fields[Input.PRICE], fields[Input.EXCHANGE_RATE])
                self.price_buy_orig = fields[Input.PRICE]
                self.price_sell = DEFAULT_DECIMAL
                self.price_sell_orig = DEFAULT_DECIMAL
                self.shares_buy = fields[Input.QUANTITY]
                self.shares_sell = DEFAULT_INT
                #TODO: commission and tax from T_RATE, when fields[Input.AUTOMATIC_FLAG] is 1
                self.commission_buy = fields[Input.COMMISSION]
                self.commission_sell = DEFAULT_DECIMAL
                self.tax_buy = fields[Input.TAX]
                self.tax_sell = DEFAULT_DECIMAL
            else:
                self.id_buy = -1
                self.id_sell = self.finance_id
                self.date_sell = self.date_created
                self.date_buy = string_to_date(DEFAULT_DATE)
                self.price_buy = DEFAULT_DECIMAL
                self.price_buy_orig = DEFAULT_DECIMAL
                self.price_sell = calc.convert_from_orig(fields[Input.PRICE], fields[Input.EXCHANGE_RATE]);
                self.price_sell_orig = fields[Input.PRICE];
                self.shares_buy = DEFAULT_INT
                self.shares_sell = fields[Input.QUANTITY]
                self.commission_buy = DEFAULT_DECIMAL
                # TODO: commission and tax from T_RATE (see also higher)
                self.commission_sell = fields[Input.COMMISSION]
                self.tax_buy = DEFAULT_DECIMAL
                self.tax_sell = fields[Input.TAX]
            self.stoploss = calc.calculate_stoploss(
                abs(fields[Input.PRICE]),
                fields[Input.QUANTITY],
                fields[Input.TAX],
                fields[Input.COMMISSION],
                fields[Input.RISK],
                fields[Input.POOL],
                self.long_flag)
            self.stoploss_orig = calc.convert_to_orig(self.stoploss, fields[Input.EXCHANGE_RATE])
            self.profit_loss = DEFAULT_DECIMAL #Only calculated at end of trade.
            self.pool_at_start = fields[Input.POOL]
            self.amount_buy_simple = calc.calculate_amount_simple(
                Decimal(fields[Input.PRICE])
                , Decimal(fields[Input.QUANTITY]))
            self.amount_sell_simple = DEFAULT_DECIMAL
            self.risk_input = calc.calculate_risk_input(
                fields[Input.POOL],
                fields[Input.RISK])
            self.risk_input_percent = fields[Input.RISK]
            self.risk_initial = calc.calculate_risk_initial(
                fields[Input.PRICE],
                fields[Input.QUANTITY],
                fields[Input.TAX],
                fields[Input.COMMISSION],
                self.stoploss,
                self.long_flag)
            self.risk_initial_percent = Decimal(100.0)*self.risk_initial/self.amount_buy_simple
            self.risk_actual = DEFAULT_DECIMAL
            self.risk_actual_percent = DEFAULT_DECIMAL
            self.cost_total = DEFAULT_DECIMAL
            self.cost_other = DEFAULT_DECIMAL
            self.win_flag = -1 #not yet finished, we can not know it yet.
            self.currency_exchange_id = dba.first_currency_exchange_id_from_latest()
            self.drawdown_id = dba.new_drawdown_record()
            self.r_multiple = DEFAULT_DECIMAL
            date_expiration = fields[Input.DATE_EXPIRATION]
            expired_flag = DEFAULT_INT
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_TRADE, ex

    def general_info_at_end(self, fields, trade_record):
        """
            General info at the end of the trade.
        """
        try:
            self.profit_loss_percent = self.profit_loss/Decimal(100.0)
            self.year_buy = self.date_buy.year
            self.month_buy = self.date_buy.month
            self.day_buy = self.date_buy.day
            self.year_sell = self.date_sell.year
            self.month_sell = self.date_sell.month
            self.day_sell = self.date_sell.day
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_TRADE, ex

    def add_to_statement(self, records):
        """
            Add the data to the statement list.
        """
        self.statement_trade.add(
            records,
            {
                'trade_id':self.trade_id,
                'market_id':int(self.market_id),
                'commodity_name_id':int(self.commodity_name_id),
                'date_buy':self.date_buy,
                'year_buy':self.year_buy,
                'month_buy':self.month_buy,
                'day_buy':self.day_buy,
                'date_sell':self.date_sell,
                'year_sell':self.year_sell,
                'month_sell':self.month_sell,
                'day_sell':self.day_sell,
                'long_flag':int(self.long_flag),
                'price_buy':Decimal(self.price_buy),
                'price_sell':Decimal(self.price_sell),
                'shares_buy':int(self.shares_buy),
                'shares_sell':int(self.shares_sell),
                'commission_buy':Decimal(self.commission_buy),
                'commission_sell':Decimal(self.commission_sell),
                'tax_buy':Decimal(self.tax_buy),
                'tax_sell':Decimal(self.tax_sell),
                'risk_input':Decimal(self.risk_input),
                'risk_input_percent':Decimal(self.risk_input_percent),
                'risk_initial':Decimal(self.risk_initial),
                'risk_initial_percent':Decimal(self.risk_initial_percent),
                'risk_actual':Decimal(self.risk_actual),
                'risk_actual_percent':Decimal(self.risk_actual_percent),
                'cost_total':Decimal(self.cost_total),
                'cost_other':Decimal(self.cost_other),
                'amount_buy_simple':Decimal(self.amount_buy_simple),
                'amount_sell_simple':Decimal(self.amount_sell_simple),
                'stoploss':Decimal(self.stoploss),
                'profit_loss':Decimal(self.profit_loss),
                'profit_loss_percent':Decimal(self.profit_loss_percent),
                'r_multiple':Decimal(self.r_multiple),
                'win_flag':int(self.win_flag),
                'id_buy':int(self.id_buy),
                'id_sell':int(self.id_sell),
                'currency_exchange_id':int(self.currency_exchange_id),
                'drawdown_id':int(self.drawdown_id),
                'pool_at_start':Decimal(self.pool_at_start),
                'date_expiration':self.date_expiration,
                'expired_flag':self.expired_flag,
                'active':1,
                'date_created':self.date_created,
                'date_modified':self.date_modified
            },
            self.flag_insupdel
        ) 

    def print_test_info(self):
        """
            Print test info.
        """
        print('<print>')
        print('market_id =', self.market_id)
        print('commodity_name_id =', self.commodity_name_id)
        print('date_buy =', self.date_buy)
        print('date_sell =', self.date_sell)
        print('long_flag =', self.long_flag)
        print('price_buy =', self.price_buy)
        print('price_sell =', self.price_sell)
        print('risk_input =', self.risk_input)
        print('risk_input_percent =', self.risk_input_percent)
        print('risk_initial =', self.risk_initial)
        print('risk_initial_percent =', self.risk_initial_percent)
        print('risk_actual =', self.risk_actual)
        print('risk_actual_percent =', self.risk_actual_percent)
        print('cost_total =', self.cost_total)
        print('cost_other =', self.cost_other)
        print('amount_buy_simple =', self.amount_buy_simple)
        print('amount_sell_simple =', self.amount_sell_simple)
        print('stoploss =', self.stoploss)
        print('profit_loss =', self.profit_loss)
        print('profit_loss_percent =', self.profit_loss_percent)
        print('r_multiple =', self.r_multiple)
        print('win_flag =', self.win_flag)
        print('id_buy =', self.id_buy)
        print('id_sell =', self.id_sell)
        print('currency_exchange_id =', self.currency_exchange_id)
        print('drawdown_id =', self.drawdown_id)
        print('pool_at_start =', self.pool_at_start)
        print('date_expiration =', self.date_expiration)
        print('expired_flag =', self.expired_flag)
        print('<\print>')


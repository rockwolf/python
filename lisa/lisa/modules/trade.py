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
from generic.modules.calculator_finance import *

class Trade(CoreModule):
    """
        Trade class.
    """
    #NOTE: Correct way of updating =  Supplier.query.filter(<your stuff here, or user filter_by, or whatever is in your where clause>).update(values)
    #e.g.: session.query(Supplier).filter_by(id=2).update({"name": u"Mayowa"})
    #TABLE_TRADE.query.filter(market_name=...,commodity_name=...).update({"date_...": date_... etc.})
    #TODO: create seperate application that manages T_DRAWDOWN based on selection
    #where win_flag = -1
    def create_statements(self, input_fields, statements_finance):
        """
            Creates the records needed for Table.TRADE and returns them as a
            Statement object.
        """
        #NOTE: price_buy will be fields['i_amount']
        #When we buy more, it will be overwritten!
        #Trading without adding to positions is assumed by this code!
        try:
            dba = DatabaseAccess(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_trade = Statement(Table.TRADE)
            records = 0
            finance_id = dba.first_finance_id_from_latest()
            if finance_id != -1:
                for fields in input_fields:
                    #TODO: is_an_investment?
                    #TODO: check which parts are actually different from
                    #updating T_INVEST (the less difference, the better)
                    #TODO: try to separate the differences
                    #TODO: make an Invade class, where Trade and Invest
                    # inherit from.
                    if is_a_trade(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):            
                        record = records + 1
                        # GENERAL INFO
                        market_id = dba.market_id_from_market(
                                fields[Input.MARKET_CODE])
                        commodity_name_id = dba.commodity_name_id_from_commodity_name(
                                fields[Input.COMMODITY_NAME], market_id)
                        finance_record = dba.get_finance_record(finance_id)
                        trade_record = dba.get_invade_record(finance_id, T_TRADE)
                        long_flag = dba.get_long_flag_value(fields[Input.ACCOUNT_FROM],
                                fields[Input.ACCOUNT_TO], trade_record)
                        # TEST INFO
                        print('test finance_record=', finance_record)
                        print('test trade_record=', trade_record)
                        print('test: long_flag =', long_flag)

                        if dba.invade_already_started(market_id,
                                commodity_name_id, T_TRADE):
                            # UPDATE
                            flag_insupdel = Statement.UPDATE
                            trade_id = trade_record['trade_id']
                            ## buy/sell related fields
                            # TODO: the below should now be fields['i_account_from'] in TRADING_ACCOUNTS for buying
                            # ..._to']... for selling
                            if we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]) \
                                and T_TRADE.id_buy == -1:
                                id_buy = finance_id
                                id_sell = trade_record['id_sell']
                                date_buy = date_created
                                date_sell = trade_record['date_sell']
                                price_buy = abs(fields[Input.PRICE])
                                price_sell = abs(trade_record['price_sell'])
                                shares_buy = fields[Input.QUANTITY]
                                shares_sell = trade_record['shares_sell']
                                commission_buy = fields[Input.COMMISSION]
                                commission_sell = trade_record['commission_sell']
                                tax_buy = fields[Input.TAX]
                                tax_sell = trade_record['tax_sell']
                            elif not we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO])\
                                and T_TRADE.id_sell == -1:
                                id_buy = trade_record['id_buy']
                                id_sell = finance_id
                                date_buy = trade_record['date_buy']
                                date_sell = date_created
                                price_buy = abs(trade_record['price_buy'])
                                price_sell = abs(fields[Input.PRICE])
                                shares_buy = trade_record['shares_buy']
                                shares_sell = fields[Input.QUANTITY]
                                commission_buy = trade_record['commission_buy']
                                commission_sell = fields[Input.COMMISSION]
                                tax_buy = trade_record['tax_buy']
                                tax_sell = fields[Input.TAX]
                            else:
                                raise Exception(
                                    "{0} already contains a sell or buy record" \
                                    " and you are trying to add one like it" \
                                    " again?".format(T_TRADE))
                            stoploss = trade_record['stoploss']
                            profit_loss = calculate_profit_loss(
                                trade_record['amount_sell'],
                                trade_record['amount_buy'])
                            pool_at_start = \
                                trade_record['pool_at_start']
                            date_created = trade_record['date_created']
                            amount_buy_simple = trade_record['amount_buy_simple']
                            amount_sell_simple = calculate_amount_simple(
                                    Decimal(fields[Input.PRICE])
                                    , Decimal(fields[Input.QUANTITY]))
                            risk_input = trade_record['risk_input']
                            risk_input_percent = trade_record['risk_input_percent']
                            risk_initial = trade_record['risk_initial']
                            risk_initial_percent = (risk_initial/amount_buy_simple)*Decimal(100.0)
                            print('test: amount_buy_simple =', amount_buy_simple)
                            risk_actual = calculate_risk_actual(
                                trade_record['price_buy'],
                                trade_record['shares_buy'],
                                trade_record['price_sell'],
                                trade_record['shares_sell'],
                                trade_record['stoploss'],
                                trade_record['risk_initial'])
                            risk_actual_percent = (risk_actual/amount_buy_simple)*Decimal(100.0)
                            cost_total = calculate_cost_total(
                                trade_record['tax_buy'],
                                trade_record['commission_buy'],
                                trade_record['tax_sell'],
                                trade_record['commission_sell'])
                            cost_other = calculate_cost_other(
                                    cost_total,
                                    profit_loss)
                            if we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                                win_flag = dba.get_win_flag_value(
                                        price_buy,
                                        trade_record['price_sell'],
                                        long_flag)
                            else:
                                win_flag = dba.get_win_flag_value(
                                        trade_record['price_buy'],
                                        price_sell,
                                        long_flag)
                            currency_exchange_id = trade_record['currency_exchange_id']
                            drawdown_id = trade_record['drawdown_id']
                            r_multiple = calculate_r_multiple(
                                trade_record['price_buy'],
                                trade_record['price_sell'],
                                trade_record['price_stoploss'])
                            date_expiration = trade_record['date_expiration']
                            #TODO: for investing, id_buy/sell is id_firstbuy and id_firstsell
                            # and expiration flag should only be set at the end of the trade, when
                            # the trade is closed. This means that date_buy and date_sell is not
                            # enough to determine if a trade is closed or not. The total shares
                            # should also be 0 when added up OR shares_buy = shares_sell.
                            # So add:
                            #if trade_closed: (or something like that)
                            expired_flag = (1 if date_sell > date_expiration else 0)
                        else:
                            # INSERT
                            flag_insupdel = Statement.INSERT
                            trade_id = None # insert: new one created automatically
                            ## buy/sell related fields
                            if we_are_buying(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                                id_buy = finance_id
                                id_sell = -1
                                date_buy = date_created
                                date_sell = string_to_date(DEFAULT_DATE)
                                price_buy = abs(fields[Input.PRICE])
                                price_sell = DEFAULT_DECIMAL
                                shares_buy = fields[Input.QUANTITY]
                                shares_sell = DEFAULT_INT
                                commission_buy = fields[Input.COMMISSION]
                                commission_sell = DEFAULT_DECIMAL
                                tax_buy = fields[Input.TAX]
                                tax_sell = DEFAULT_DECIMAL
                            else:
                                id_buy = -1
                                id_sell = finance_id
                                date_sell = date_created
                                date_buy = string_to_date(DEFAULT_DATE)
                                price_buy = DEFAULT_DECIMAL
                                price_sell = abs(fields[Input.PRICE])
                                shares_buy = DEFAULT_INT
                                shares_sell = fields[Input.QUANTITY]
                                commission_buy = DEFAULT_DECIMAL
                                commission_sell = fields[Input.COMMISSION]
                                tax_buy = DEFAULT_DECIMAL
                                tax_sell = fields[Input.TAX]
                            print(library_test())
                            print('TEST stoploss:(price, shares, tax, comm, risk_input, pool) = '
                                    , fields[Input.PRICE]
                                    , fields[Input.QUANTITY]
                                    , fields[Input.TAX]
                                    , fields[Input.COMMISSION]
                                    , fields[Input.RISK]
                                    , fields[Input.POOL])
                            stoploss = calculate_stoploss(
                                abs(fields[Input.PRICE]),
                                fields[Input.QUANTITY],
                                fields[Input.TAX],
                                fields[Input.COMMISSION],
                                fields[Input.RISK],
                                fields[Input.POOL])
                            profit_loss = DEFAULT_DECIMAL #Only calculated at end of trade.
                            pool_at_start = fields[Input.POOL]
                            print('test: i_price =', fields[Input.PRICE])
                            print('test: i_shares =', fields[Input.QUANTITY])
                            amount_buy_simple = calculate_amount_simple(
                                    Decimal(fields[Input.PRICE])
                                    , Decimal(fields[Input.QUANTITY]))
                            amount_sell_simple = DEFAULT_DECIMAL
                            print('test E')
                            risk_input = calculate_risk_input(
                                fields[Input.POOL],
                                fields[Input.RISK])
                            risk_input_percent = fields[Input.RISK]
                            print('test F')
                            risk_initial = calculate_risk_initial(
                                fields[Input.PRICE],
                                fields[Input.QUANTITY],
                                stoploss)
                            print('test: price, shares, stoploss = ', fields[Input.PRICE], fields[Input.QUANTITY], stoploss)
                            print('test amount_buy_simple = ', amount_buy_simple)
                            risk_initial_percent = Decimal(100.0)*risk_initial/amount_buy_simple
                            risk_actual = DEFAULT_DECIMAL
                            risk_actual_percent = DEFAULT_DECIMAL
                            cost_total = DEFAULT_DECIMAL
                            cost_other = DEFAULT_DECIMAL
                            win_flag = -1 #not yet finished, we can not know it yet.
                            currency_exchange_id = dba.first_currency_exchange_id_from_latest()
                            drawdown_id = dba.new_drawdown_record()
                            r_multiple = DEFAULT_DECIMAL
                            date_expiration = fields[Input.DATE_EXPIRATION]
                            expired_flag = DEFAULT_INT
                                
                        # GENERAL VARIABLES THAT CAN BE CALCULATED ON THE DATA WE HAVE
                        profit_loss_percent = profit_loss/Decimal(100.0)
                        year_buy = date_buy.year
                        month_buy = date_buy.month
                        day_buy = date_buy.day
                        year_sell = date_sell.year
                        month_sell = date_sell.month
                        day_sell = date_sell.day
                        
                        # TEST INFO
                        print('<print>')
                        print('market_id =', market_id)
                        print('commodity_name_id =', commodity_name_id)
                        print('date_buy =', date_buy)
                        print('date_sell =', date_sell)
                        print('long_flag =', long_flag)
                        print('price_buy =', price_buy)
                        print('price_sell =', price_sell)
                        print('risk_input =', risk_input)
                        print('risk_input_percent =', risk_input_percent)
                        print('risk_initial =', risk_initial)
                        print('risk_initial_percent =', risk_initial_percent)
                        print('risk_actual =', risk_actual)
                        print('risk_actual_percent =', risk_actual_percent)
                        print('cost_total =', cost_total)
                        print('cost_other =', cost_other)
                        print('amount_buy_simple =', amount_buy_simple)
                        print('amount_sell_simple =', amount_sell_simple)
                        print('stoploss =', stoploss)
                        print('profit_loss =', profit_loss)
                        print('profit_loss_percent =', profit_loss_percent)
                        print('r_multiple =', r_multiple)
                        print('win_flag =', win_flag)
                        print('id_buy =', id_buy)
                        print('id_sell =', id_sell)
                        print('currency_exchange_id =', currency_exchange_id)
                        print('drawdown_id =', drawdown_id)
                        print('pool_at_start =', pool_at_start)
                        print('date_expiration =', date_expiration)
                        print('expired_flag =', expired_flag)
                        print('<\print>')
                        
                        # ADDING THE STATEMENTS
                        statement_trade.add(
                            records,
                            {
                                'trade_id':trade_id,
                                'market_id':int(market_id),
                                'commodity_name_id':int(commodity_name_id),
                                'date_buy':date_buy,
                                'year_buy':year_buy,
                                'month_buy':month_buy,
                                'day_buy':day_buy,
                                'date_sell':date_sell,
                                'year_sell':year_sell,
                                'month_sell':month_sell,
                                'day_sell':day_sell,
                                'long_flag':int(long_flag),
                                'price_buy':Decimal(price_buy),
                                'price_sell':Decimal(price_sell),
                                'shares_buy':int(shares_buy),
                                'shares_sell':int(shares_sell),
                                'commission_buy':Decimal(commission_buy),
                                'commission_sell':Decimal(commission_sell),
                                'tax_buy':Decimal(tax_buy),
                                'tax_sell':Decimal(tax_sell),
                                'risk_input':Decimal(risk_input),
                                'risk_input_percent':Decimal(risk_input_percent),
                                'risk_initial':Decimal(risk_initial),
                                'risk_initial_percent':Decimal(risk_initial_percent),
                                'risk_actual':Decimal(risk_actual),
                                'risk_actual_percent':Decimal(risk_actual_percent),
                                'cost_total':Decimal(cost_total),
                                'cost_other':Decimal(cost_other),
                                'amount_buy_simple':Decimal(amount_buy_simple),
                                'amount_sell_simple':Decimal(amount_sell_simple),
                                'stoploss':Decimal(stoploss),
                                'profit_loss':Decimal(profit_loss),
                                'profit_loss_percent':Decimal(profit_loss_percent),
                                'r_multiple':Decimal(r_multiple),
                                'win_flag':int(win_flag),
                                'id_buy':int(id_buy),
                                'id_sell':int(id_sell),
                                'currency_exchange_id':int(currency_exchange_id),
                                'drawdown_id':int(drawdown_id),
                                'pool_at_start':
                                    Decimal(pool_at_start),
                                'date_expiration': date_expiration,
                                'expired_flag': expired_flag,
                                'active':1,
                                'date_created':date_created,
                                'date_modified':date_modified
                            },
                            flag_insupdel
                        )    
                finance_id = finance_id + 1
            return statement_trade
        except Exception as ex:
            print(Error.CREATE_STATEMENTS_TABLE_TRADE, ex)
        finally:
            dba = None

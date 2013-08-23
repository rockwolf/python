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
from database.mappings import T_INVESTMENT
from modules_generic.calculator_finance import *

class Investment(CoreModule):
    """
        Investment class.
    """

    #TODO: this needs to be a portfolio module, but
    #we don't need it at the moment. Will be finished
    #later. T_STOCK is no longer needed, it will be T_INVEST.
    #TODO: finishing just happens! Try to figure out how to
    #skip the investing part so we can figure out a way to
    #finish it later. Perhaps keep the records in a spreadsheet
    #and manually insert them later?
    #unless offcourse it's easier to just implement it. It's identical
    #to T_TRADE anyway, except for a few fields.
    #NOTE: convention: 0 = insert / 1 = update / 3 = delete
    def create_statements(self, input_fields, statements_finance):
        """
            Creates the records needed for Table.INVESTMENT and returns them as a
            Statement object.
        """
        #NOTE: price_buy will be fields['amount']
        #When we buy more, it will be overwritten!
        #Trading without adding to positions is assumed by this code!
        #But this is investing, so we need to deal with that shit!
        try:
            dba = DatabaseAcces(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_invest = Statement(Table.INVESTMENT)
            records = 0
            finance_id = dba.first_finance_id_from_latest()
            if finance_id != -1:
                for fields in input_fields:
                    if is_an_investment(fields['i_account_from'], fields['i_account_to']):            
                        record = records + 1
                        # GENERAL INFO
                        market_id = dba.market_id_from_market(
                                fields['i_market_name'])
                        stock_name_id = dba.stock_name_id_from_stock_name(
                                fields['i_stock_name'], market_id)
                        finance_record = dba.get_finance_record(finance_id)
                        #TODO: this is WRONG!
                        #it's based on the link between id_buy and id_sell,
                        #but for investing, this is id_buy for the first buy
                        #and not the next ones!
                        #This is really becoming more complex than necessary,
                        #split the code and focus on T_TRADE instead.
                        investment_record = dba.get_invade_record(finance_id, Table.INVESTMENT)
                        long_flag = dba.get_long_flag_value(fields['i_category'],
                                fields['i_subcategory'], investment_record)
                        # TEST INFO
                        print('test finance_record=', finance_record)
                        print('test investment_record=', investment_record)
                        print('test: long_flag =', long_flag)

                        if dba.invade_already_started(market_id,
                                stock_name_id, T_INVESTMENT):
                            # UPDATE
                            flag_insupdel = STatement.UPDATE
                            investment_id = investment_record['investment_id']
                            ## buy/sell related fields
                            if we_are_buying(fields['i_account_from'], fields['i_account_to']) \
                                and T_TRADE.id_buy == -1:
                                id_buy = finance_id
                                id_sell = investment_record['id_sell']
                                date_buy = date_created
                                date_sell = investment_record['date_sell']
                                price_buy = abs(fields['i_price'])
                                price_sell = abs(investment_record['price_sell'])
                                shares_buy = fields['i_shares']
                                shares_sell = investment_record['shares_sell']
                                commission_buy = fields['i_commission']
                                commission_sell = investment_record['commission_sell']
                                tax_buy = fields['i_tax']
                                tax_sell = investment_record['tax_sell']
                            elif not we_are_buying(fields['i_account_from'], fields['i_account_to']) \
                                and T_TRADE.id_sell == -1:
                                id_buy = investment_record['id_buy']
                                id_sell = finance_id
                                date_buy = investment_record['date_buy']
                                date_sell = date_created
                                price_buy = abs(investment_record['price_buy'])
                                price_sell = abs(fields['i_price'])
                                shares_buy = investment_record['shares_buy']
                                shares_sell = fields['i_shares']
                                commission_buy = investment_record['commission_buy']
                                commission_sell = fields['i_commission']
                                tax_buy = investment_record['tax_buy']
                                tax_sell = fields['i_tax']
                            else:
                                raise Exception(
                                    "{0} already contains a sell or buy record" \
                                    " and you are trying to add one like it" \
                                    " again?".format(Table.TRADE))
                            stoploss = investment_record['stoploss']
                            profit_loss = calculate_profit_loss(
                                investment_record['amount_sell'],
                                investment_record['amount_buy'])
                            pool_at_start = \
                                investment_record['pool_at_start']
                            date_created = investment_record['date_created']
                            amount_buy_simple = investment_record['amount_buy_simple']
                            amount_sell_simple = calculate_amount_simple(
                                    Decimal(fields['i_shares']),
                                    Decimal(fields['i_shares']))
                            risk_input = investment_record['risk_input']
                            risk_input_percent = investment_record['risk_input_percent']
                            risk_initial = investment_record['risk_initial']
                            risk_initial_percent = (risk_initial/amount_buy_simple)*100.0
                            risk_actual = calculate_risk_actual(
                                investment_record['price_buy'],
                                investment_record['shares_buy'],
                                investment_record['price_sell'],
                                investment_record['shares_sell'],
                                investment_record['stoploss'],
                                investment_record['risk_initial'])
                            risk_actual_percent = (risk_actual/amount_buy_simple)*100.0
                            cost_total = calculate_cost_total(
                                investment_record['tax_buy'],
                                investment_record['commission_buy'],
                                investment_record['tax_sell'],
                                investment_record['commission_sell'])
                            cost_other = calculate_cost_other(
                                    cost_total,
                                    profit_loss)
                            if we_are_buying(fields['i_account_from'], fields['i_account_to']):
                                win_flag = dba.get_win_flag_value(
                                        price_buy,
                                        investment_record['price_sell'],
                                        long_flag)
                            else:
                                win_flag = dba.get_win_flag_value(
                                        investment_record['price_buy'],
                                        price_sell,
                                        long_flag)
                            from_currency_id = investment_record['from_currency_id']
                            drawdown_id = investment_record['drawdown_id']
                            r_multiple = calculate_r_multiple(
                                investment_record['price_buy'],
                                investment_record['price_sell'],
                                investment_record['price_stoploss'])
                            date_expiration = investment_record['date_expiration']
                            #TODO: for investing, id_buy/sell is id_firstbuy and id_firstsell
                            # and expiration flag should only be set at the end of the trade, when
                            # the trade is closed. This means that date_buy and date_sell is not
                            # enough to determine if a trade is closed or not. The total shares
                            # should also be 0 when added up OR shares_buy = shares_sell.
                            # So add:
                            #if trade_closed: (or something like that)
                            expired_flag = (1 if date_sell > date_expiration else 0)
                            spread = investment_record['spread']
                        else:
                            # INSERT
                            flag_insupdel = STATEMENT_INSERT
                            investment_id = None # insert: new one created automatically
                            ## buy/sell related fields
                            if we_are_buying(fields['i_account_from'], fields['i_account_to']):
                                id_buy = finance_id
                                id_sell = -1
                                date_buy = date_created
                                date_sell = string_to_date(DEFAULT_DATE)
                                price_buy = abs(fields['i_price'])
                                price_sell = DEFAULT_DECIMAL
                                shares_buy = fields['i_shares']
                                shares_sell = DEFAULT_INT
                                commission_buy = fields['i_commission']
                                commission_sell = DEFAULT_DECIMAL
                                tax_buy = fields['i_tax']
                                tax_sell = DEFAULT_DECIMAL
                            else:
                                id_buy = -1
                                id_sell = finance_id
                                date_sell = date_created
                                date_buy = string_to_date(DEFAULT_DATE)
                                price_buy = DEFAULT_DECIMAL
                                price_sell = abs(fields['i_price'])
                                shares_buy = DEFAULT_INT
                                shares_sell = fields['i_shares']
                                commission_buy = DEFAULT_DECIMAL
                                commission_sell = fields['i_commission']
                                tax_buy = DEFAULT_DECIMAL
                                tax_sell = fields['tax']
                            stoploss = calculate_stoploss(
                                fields['i_amount'],
                                fields['i_shares'],
                                fields['i_tax'],
                                fields['i_commission'],
                                fields['i_risk_input'],
                                fields['i_pool']
                                )
                            profit_loss = DEFAULT_DECIMAL #Only calculated at end of trade.
                            pool_at_start = fields['i_pool']
                            amount_buy_simple = calculate_amount_simple(
                                    Decimal(fields['i_price'])
                                    , Decimal(fields['i_shares']))
                            amount_sell_simple = DEFAULT_DECIMAL
                            risk_input = calculate_risk_input(
                                fields['i_pool'],
                                fields['i_risk_input'])
                            risk_input_percent = fields['i_risk_input']
                            risk_initial = calculate_risk_initial(
                                fields['i_price'],
                                fields['i_shares'],
                                stoploss)
                            risk_initial_percent = risk_initial/amount_buy_simple
                            risk_actual = DEFAULT_DECIMAL
                            risk_actual_percent = DEFAULT_DECIMAL
                            cost_total = DEFAULT_DECIMAL
                            cost_other = DEFAULT_DECIMAL
                            win_flag = -1 #not yet finished, we can not know it yet.
                            from_currency_id = dba.currency_id_from_currency(fields['i_currency_from'])
                            drawdown_id = dba.new_drawdown_record()
                            r_multiple = DEFAULT_DECIMAL
                            date_expiration = fields['i_date_expiration']
                            expired_flag = DEFAULT_INT
                            spread = DEFAULT_DECIMAL
                                
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
                        print('stock_name_id =', stock_name_id)
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
                        print('stoploss =', stoploss)
                        print('profit_loss =', profit_loss)
                        print('profit_loss_percent =', profit_loss_percent)
                        print('r_multiple =', r_multiple)
                        print('win_flag =', win_flag)
                        print('amount_buy_simple =', amount_buy_simple)
                        print('amount_sell_simple =', amount_sell_simple)
                        print('id_buy =', id_buy)
                        print('id_sell =', id_sell)
                        print('from_currency_id =', from_currency_id)
                        print('drawdown_id =', drawdown_id)
                        print('pool_at_start =', pool_at_start)
                        print('date_expiration =', date_expiration)
                        print('expired_flag =', expired_flag)
                        print('spread =', spread)
                        print('<\print>')
                        
                        # ADDING THE STATEMENTS
                        statement_trade.add(
                            records,
                            {
                                'trade_id':trade_id,
                                'market_id':int(market_id),
                                'stock_name_id':int(stock_name_id),
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
                                'from_currency_id':int(from_currency_id),
                                'drawdown_id':int(drawdown_id),
                                'pool_at_start':
                                    Decimal(pool_at_start),
                                'date_expiration': date_expiration,
                                'expired_flag': expired_flag,
                                'spread': spread,
                                'active':1,
                                'date_created':date_created,
                                'date_modified':date_modified
                            },
                            flag_insupdel
                        )    
                finance_id = finance_id + 1
            return statement_trade
        except Exception as ex:
            print(Error.CREATE_STATEMENTS_TABLE_INVESTMENT, ex)
        finally:
            dba = None

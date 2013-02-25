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
            Creates the records needed for TABLE_INVESTMENT and returns them as a
            Statement object.
        """
        #NOTE: price_buy will be fields['amount']
        #When we buy more, it will be overwritten!
        #Trading without adding to positions is assumed by this code!
        #But this is investing, so we need to deal with that shit!
        try:
            session = self.Session()
            dba = DatabaseAcces(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_invest = Statement(TABLE_INVESTMENT)
            records = 0
            finance_id = dba.first_finance_id_from_latest()
            if finance_id != -1:
                for fields in input_fields:
                    if is_an_investment(fields['category'], fields['subcategory']):            
                        record = records + 1
                        # GENERAL INFO
                        market_id = dba.market_id_from_market(
                                fields['market_name'])
                        stock_name_id = dba.stock_name_id_from_stock_name(
                                fields['stock_name'], market_id)
                        finance_record = dba.get_finance_record(finance_id)
                        #TODO: this is WRONG!
                        #it's based on the link between id_buy and id_sell,
                        #but for investing, this is id_buy for the first buy
                        #and not the next ones!
                        #This is really becoming more complex than necessary,
                        #split the code and focus on T_TRADE instead.
                        investment_record = dba.get_investment_record(finance_id)
                        long_flag = dba.get_long_flag_value(fields['category'],
                                fields['subcategory'], investment_record)
                        # TEST INFO
                        print('test finance_record=', finance_record)
                        print('test investment_record=', investment_record)
                        print('test: long_flag =', long_flag)

                        if dba.invade_already_started(market_id,
                                stock_name_id, T_INVESTMENT):
                            # UPDATE
                            flag_insupdel = STATEMENT_UPDATE
                            trade_id = investment_record['trade_id']
                            ## buy/sell related fields
                            if fields['subcategory'] == 'buy' \
                                and T_TRADE.id_buy == -1:
                                id_buy = finance_id
                                id_sell = investment_record['id_sell']
                                date_buy = date_created
                                date_sell = investment_record['date_sell']
                                price_buy = abs(fields['price'])
                                price_sell = abs(investment_record['price_sell'])
                                shares_buy = fields['shares']
                                shares_sell = investment_record['shares_sell']
                                commission_buy = fields['commission']
                                commission_sell = investment_record['commission_sell']
                                tax_buy = fields['tax']
                                tax_sell = investment_record['tax_sell']
                            elif fields['subcategory'] == 'sell' \
                                and T_TRADE.id_sell == -1:
                                id_buy = investment_record['id_buy']
                                id_sell = finance_id
                                date_buy = investment_record['date_buy']
                                date_sell = date_created
                                price_buy = abs(investment_record['price_buy'])
                                price_sell = abs(fields['price'])
                                shares_buy = investment_record['shares_buy']
                                shares_sell = fields['shares']
                                commission_buy = investment_record['commission_buy']
                                commission_sell = fields['commission']
                                tax_buy = investment_record['tax_buy']
                                tax_sell = fields['tax']
                            else:
                                raise Exception(
                                    "{0} already contains a sell or buy record" \
                                    " and you are trying to add one like it" \
                                    " again?".format(TABLE_TRADE))
                            stoploss = investment_record['stoploss']
                            profit_loss = dba.calculate_profit_loss(fields)
                            pool_at_start = \
                                investment_record['pool_at_start']
                            date_created = investment_record['date_created']
                            at_work = investment_record['at_work']
                            risk_input = investment_record['risk_input']
                            risk_input_percent = investment_record['risk_input_percent']
                            risk_initial = investment_record['risk_initial']
                            risk_initial_percent = (risk_initial/at_work)*100.0
                            risk_actual = dba.calculate_risk_actual(investment_record, stoploss)
                            risk_actual_percent = (risk_actual/at_work)*100.0
                            cost_total = dba.calculate_cost_total(investment_record)
                            #TODO: check http://stackoverflow.com/questions/270879/efficiently-updating-database-using-sqlalchemy-orm
                            if we_are_buying(fields['subcategory']):
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
                            r_multiple = dba.calculate_r_multiple()
                            date_expiration = investment_record['date_expiration']
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
                            flag_insupdel = STATEMENT_INSERT
                            trade_id = None # insert: new one created automatically
                            ## buy/sell related fields
                            if we_are_buying(fields['subcategory']):
                                id_buy = finance_id
                                id_sell = -1
                                date_buy = date_created
                                date_sell = string_to_date(DEFAULT_DATE)
                                price_buy = abs(fields['price'])
                                price_sell = DEFAULT_DECIMAL
                                shares_buy = fields['shares']
                                shares_sell = DEFAULT_INT
                                commission_buy = fields['commission']
                                commission_sell = DEFAULT_DECIMAL
                                tax_buy = fields['tax']
                                tax_sell = DEFAULT_DECIMAL
                            else:
                                id_buy = -1
                                id_sell = finance_id
                                date_sell = date_created
                                date_buy = string_to_date(DEFAULT_DATE)
                                price_buy = DEFAULT_DECIMAL
                                price_sell = abs(fields['price'])
                                shares_buy = DEFAULT_INT
                                shares_sell = fields['shares']
                                commission_buy = DEFAULT_DECIMAL
                                commission_sell = fields['commission']
                                tax_buy = DEFAULT_DECIMAL
                                tax_sell = fields['tax']
                            stoploss = dba.calculate_stoploss(fields)
                            profit_loss = DEFAULT_DECIMAL #Only calculated at end of trade.
                            pool_at_start = \
                                fields['pool_trading']
                            at_work = Decimal(price_buy)*Decimal(fields['shares'])
                            risk_input = dba.calculate_risk_input(fields)
                            risk_input_percent = fields['risk_input']
                            risk_initial = dba.calculate_risk_initial(fields,
                                    stoploss)
                            risk_initial_percent = risk_initial/at_work
                            risk_actual = DEFAULT_DECIMAL
                            risk_actual_percent = DEFAULT_DECIMAL
                            cost_total = DEFAULT_DECIMAL
                            win_flag = -1 #not yet finished, we can not know it yet.
                            from_currency_id = dba.currency_id_from_currency(fields['from_currency'])
                            drawdown_id = dba.new_drawdown_record()
                            r_multiple = DEFAULT_DECIMAL
                            date_expiration = fields['date_expiration']
                            expired_flag = DEFAULT_INTEGER
                                
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
                        print('at_work =', at_work)
                        print('id_buy =', id_buy)
                        print('id_sell =', id_sell)
                        print('from_currency_id =', from_currency_id)
                        print('drawdown_id =', drawdown_id)
                        print('pool_at_start =', pool_at_start)
                        print('date_expiration =', date_expiration)
                        print('expired_flag =', expired_flag)
                        print('<\print>')
                        
                        # ADDING THE STATEMENTS
                        #TODO: add a trade_id (retrieved above?) for the update statements.
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
                                'stoploss':Decimal(stoploss),
                                'profit_loss':Decimal(profit_loss),
                                'profit_loss_percent':Decimal(profit_loss_percent),
                                'r_multiple':Decimal(r_multiple),
                                'win_flag':int(win_flag),
                                'at_work':Decimal(at_work),
                                'id_buy':int(id_buy),
                                'id_sell':int(id_sell),
                                'from_currency_id':int(from_currency_id),
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
            print(ERROR_CREATE_STATEMENTS_TABLE_INVESTMENT, ex)
            session.rollback()
        finally:
            dba = None
            session = None
    
    def get_investment_record(self, finance_id):
        """
            Gets the investment_record with the given finance_id set in
            either id_buy or id_sell.
        """
        result = []
        session = self.Session()
        try:
            #TODO: finance_created is not used?????
            finance_created = self.get_latest_date_created(TABLE_INVESTMENT)
            first_obj = session.query(T_INVESTMENT).filter(
                    or_(
                        T_INVESTMENT.id_buy == finance_id,
                        T_INVESTMENT.id_sell == finance_id)).first() #finance_id is unique anyway
            if first_obj is not None:
                result = self.get_record(first_obj)
        except Exception as ex:
            print("Error in get_investment_record: ", ex)
        finally:
            session.rollback()
            session = None
        return result

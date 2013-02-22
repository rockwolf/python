#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""

from sqlalchemy import Table, MetaData, \
        Column, Integer, or_, and_
from sqlalchemy.types import VARCHAR
#from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime

from modules_generic.function import *
from modules_generic.function_sqlalchemy import row_to_dict
from modules_generic.messagehandler import *
from modules.statement import Statement
from modules.constant import *
from modules.function import *
from meta import engine, Base
from database.mappings import *
from database.mappings_views import *

class DatabaseAccess():
    """
        Connecting to the database.
    """ 

    def __init__(self, config):
        """
            Initialize object.
        """
        try:
            self.config = config
            self.Session = sessionmaker(bind=engine) 
            self.metadata = Base.metadata
            #self.map_tables()
            #self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if is_a_table(x) ]
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def config(self):
        """
            Retrieve config file values.
        """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
 
    def get_categories(self):
        """
            Get the categories.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_CATEGORY)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_CATEGORIES, ex)
        finally:
            session.rollback()
            session = None
        return values
    
    def get_accounts(self):
        """
            Get the accounts.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_ACCOUNT)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_ACCOUNTS, ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_subcategories(self):
        """
            Get the subcategories.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_SUBCATEGORY)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_SUBCATEGORIES, ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_markets(self):
        """
            Get the market codes.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(
                    T_MARKET.active == 1)
            for instance in query: 
                values.append(instance.code)
        except Exception as ex:
            print(ERROR_GET_MARKETS, ex)
        finally:
            session.rollback()
            session = None
        return values
 
    def get_stock_names(self, code):
        """
            Get the stock names.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_STOCK_NAME).join(
                T_MARKET, 
                T_STOCK_NAME.market_id == T_MARKET.market_id
            ).filter(
                T_MARKET.code == code,
                T_STOCK_NAME.active == 1
            )
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_stock_names: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_market_description(self, market):
        """
            Get the market description.
        """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(T_MARKET.code == market)
            for instance in query:
                value = instance.name
                break
        except Exception as ex:
            print(ERROR_GET_MARKET_DESCRIPTION, ex)
        finally:
            session.rollback()
            session = None
        return value 

    def get_stock_description(self, stock):
        """
            Get the stock description.
        """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_STOCK_NAME).filter(T_STOCK_NAME.name == stock)
            for instance in query:
                value = instance.description
                break
        except Exception as ex:
            print("Error in get_stock_description: ", ex)
        finally:
            session.rollback()
            session = None
        return value 

    def get_stockinfo(self, sname):
        """
            Get extra stock info.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(
                T_STOCK_NAME.name.label("stock_name"), 
                T_MARKET.name.label("marketname"), 
                T_MARKET.country
            ).join(
                T_MARKET, 
                T_STOCK_NAME.market_id == T_MARKET.market_id
            ).filter(
                T_STOCK_NAME.name == sname
            )
            for instance in query: 
                values.append(instance.stock_name)
                values.append(instance.marketname)
                values.append(instance.country)
        except Exception as ex:
            print(ERROR_GET_STOCK_INFO, ex)
        finally:
            session.rollback()
            session = None
        return values
     
    def get_currencies(self):
        """
            Get the currency codes.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_CURRENCY)
            for instance in query: 
                values.append(instance.code)
        except Exception as ex:
            print(ERROR_GET_CURRENCIES, ex)
        finally:
            session.rollback()
            session = None
        return values

    def create_statements_TABLE_RATE(self, input_fields):
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
   
    def calculate_stoploss(self, fields):
        """
            Calculates the stoploss.
        """
        #NOTE: ((risk/100 * pool - amount) - commission_buy)/(shares_buy * (tax/100 - 1))
        #NOTE: ((R * P - A) - C) / (S * (T - 1))
        #TODO: Get the correct tax amount here, when automatic is checked.
        R = Decimal(fields['risk_input']) / Decimal(100.0)
        P = abs(Decimal(fields['pool_trading']))
        A = abs(Decimal(fields['amount']))
        S = Decimal(fields['shares'])
        T = Decimal(fields['tax']) / Decimal(100.0)
        C = Decimal(fields['commission'])
        result = ((R * P - A) - C) / (S * (T - 1))
        return result

    def calculate_profit_loss(self, fields, trade_record):
        """
            Calculates the profit_loss.
        """
        #NOTE: sold - bought
        #NOTE: So - Bo
        #TODO: this does not seem correct, doesn't it need the tax part too?
        Bo = Decimal(trade_record['price_buy']) * Decimal(trade_record['shares_buy']) \
                + Decimal(trade_record['commission_buy'])
        So = Decimal(trade_record['price_sell']) * \
                Decimal(trade_record['shares_sell']) \
                - Decimal(trade_record['commission_sell'])
        result = So - Bo
        return result

    def calculate_risk_input(self, fields):
        """
            Calculates the risk based on total pool and input.
            Consider this the theoretical risk we want to take.
        """
        #NOTE: The pool for calculations on a single trade uses
        # amount. Think of it as a 'pool to use'. Do not confuse
        # this with the total pool available from get_trading_pool.
        # fields['risk_input']*fields['amount'] 
        #NOTE: Attention: the risk already gets divided by 100 in the
        #beginning, right after the field retrieval!
        #NOTE: (risk_input) * pool_to_use
        #NOTE: R * Pu
        R = Decimal(fields['risk_input'])/Decimal(100.0)
        Pu = abs(Decimal(fields['amount']))
        result = R * Pu
        return result

    def calculate_risk_initial(self, fields, stoploss):
        """
            Calculates the initial risk.
            This is the risk we will take if our stoploss is reached.
            This should be equal to the risk_input if everything was
            correctly calculated.
        """
        #NOTE: commission + tax = seperate = costs
        #NOTE: (price*shares) - (stoploss*shares)
        #NOTE: (P * S) - (SL * S)
        Pb = Decimal(fields['price'])
        Sb = Decimal(fields['shares'])
        SL = Decimal(stoploss)
        result = (P * Sb) - (SL * Sb)
        return result

    def calculate_risk_actual(self, trade_record, stoploss):
        """
            Calculates the risk we actually took,
            based on the data in TABLE_TRADE.
        """
        #NOTE: (price*shares) - (price_sell*shares)
        #NOTE: (Pb * Sb) - (Ps * Ss)
        #NOTE: price_sell > stoploss = max risk was the initial risk
        Pb = Decimal(fields['price_buy'])
        Sb = Decimal(fields['shares_buy'])
        Ps = Decimal(fields['price_sell'])
        Ss = Decimal(fields['shares_sell'])
        if Ps < stoploss:
            result = (Pb * Sb) - (Ps * Ss)
        else:
            result = trade_record['risk_initial']
        return result

    def calculate_cost_total(self, trade_record):
    	"""
    	    Returns the total costs associated with the given trade.
    	"""
    	return (
    	    trade_record['tax_buy'] +
    	    trade_record['commission_buy'] +
    	    trade_record['tax_sell'] +
    	    trade_record['commission_sell']
    	)

    def trade_closed(self, invade_record):
    	"""
    	    Checks if a trade/investment is closed.
    	"""
    	#NOTE: invade = can be INVestment or trADE
    	return (
            (invade_record['date_buy'] != DEFAULT_DATE)
    	    and (invade_record['date_sell'] != DEFAULT_DATE)
    	    and (invade_record['shares_buy'] == invade_record['shares_sell']))
    	
    def get_long_flag_value(self, category, subcategory, trade_record):
        """
            Are we long?
        """
        result = False
        if trade_record == []:
            result = (category == 'trade.tx' and subcategory == 'buy') 
        else:
            result = (category == 'trade.rx' and subcategory == 'sell'
                      and trade_record['date_buy'] != DEFAULT_DATE)
        return 1 if result else 0

    #TODO: toroughly test this
    def get_win_flag_value(self, price_buy, price_sell, long_flag):
        """
            Trade finished... did we win?
        """
        result = False
        if long_flag == 1:
            result = (price_buy < price_sell)
        else:
            result = (price_buy > price_sell)
        return 1 if result else 0

    def create_statements_TABLE_CURRENCY_EXCHANGE(self, input_fields):
        """
            Creates the records needed for TABLE_CURRENCY_EXCHANGE.
        """
        try:
            statement_currency_exchange = Statement(TABLE_CURRENCY_EXCHANGE)
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
                        'from_currency_id':self.currency_id_from_currency(fields['from_currency']),
                        'to_currency_id':int(self.config.default_currency),
                        'exchange_rate':Decimal(fields['exchange_rate']),
                        'date_created':date_created,
                        'date_modified':date_modified
                    }
                )
            return statement_currency_exchange
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE, ex)

    def calculate_commission(self):
        """
            Calculation for T_RATE.
        """
        return DEFAULT_DECIMAL
    
    def write_to_database(self, statements):
        """ 
            Writes the records of a given statements list to the database.
        """
        try:
            if statements != []:
                #insert
                statements_insert = self.assemble_statement_list_insert(
                        statements, 0)
                self.write_statement_list_insert(
                        statements_insert, statements.table_name)
                #update
                statements_update = self.assemble_statement_list_update(
                        statements, 1)
                self.write_statement_list_update(
                        statements_update, statements.table_name)
                #delete
                statements_delete = self.assemble_statement_list_delete(
                        statements, 2)
                self.write_statement_list_delete(
                        statements_delete, statements.table_name)
        except Exception as ex:
            print(ERROR_WRITE_TO_DATABASE_SESSION, ex)

    def write_statement_list_insert(self, final_statements, table_name):
        """
            Commit the insert statements to database.
        """
        session = self.Session()
        try:
            if final_statements != []:
                print(table_name, end=': ')
                session.add_all(final_statements)
                session.commit()
                print("{0} records added.".format(str(len(final_statements))))
                print('')
        except Exception as ex:
            print(ERROR_INSERT_DATABASE, ex)
        finally:
            session.rollback()
            session = None

    def write_statement_list_update(self, final_statements, table_name):
        """
            Execute the update statements on the database.
        """
        #TODO: this code needs the update instruction I've written somewhere
        #in databaseaccess.py
        session = self.Session()
        try:
            if final_statements != []:
                print(table_name, end=': ')
                #session.add_all(final_statements)
                #session.commit()
                for statement in final_statements:
                	print('test:', statement)
                #TODO: set the values here and commit for each record in final_statements
                print("{0} records updated.".format(str(len(final_statements))))
                print('')
        except Exception as ex:
            print(ERROR_UPDATE_DATABASE, ex)
        finally:
            session.rollback()
            session = None


    def write_statement_list_delete(self, final_statements, table_name):
        """
            Write the insert statements to database.
        """
        #TODO: finish this later. Low priority!
        pass

    def assemble_statement_list_insert(self, statements, insupdel=0):
        """
            Creates list of TABLE_NAME(..., ..., ...) records
            from new statements, that we can use to insert at once.
        """
        #TODO: find a way to refactor this piece of crap code.
        result = []
        inner_part_list = statements.get_statement_list(insupdel)
        if statements.table_name == TABLE_CURRENCY_EXCHANGE:
            for record in inner_part_list:
                result.append(T_CURRENCY_EXCHANGE(
                    record['currency_exchange_id'],
                    record['from_currency_id'],
                    record['to_currency_id'],
                    record['exchange_rate'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table_name == TABLE_RATE:
            for record in inner_part_list:
                result.append(T_RATE(
                    record['rate_id'],
                    record['calculated'],
                    record['calculated_percent'],
                    record['on_shares'],
                    record['on_commission'],
                    record['on_ordersize'],
                    record['on_other'],
                    record['commission'],
                    record['tax'],
                    record['formula_id'],
                    record['manual_flag'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table_name == TABLE_FINANCE:
            for record in inner_part_list:
                result.append(T_FINANCE(
                    record['finance_id'],
                    record['date'],
                    record['year'],
                    record['month'],
                    record['day'],
                    record['account_id'],
                    record['category_id'],
                    record['subcategory_id'],
                    record['amount'],
                    record['comment'],
                    record['stock_name_id'],
                    record['shares'],
                    record['price'],
                    record['tax'],
                    record['commission'],
                    record['active'],
                    record['rate_id'],
                    record['currency_exchange_id'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table_name == TABLE_TRADE:
            for record in inner_part_list:
                result.append(T_TRADE(
                    record['trade_id'],
                    record['market_id'],
                    record['stock_name_id'],
                    record['date_buy'],
                    record['year_buy'],
                    record['month_buy'],
                    record['day_buy'],
                    record['date_sell'],
                    record['year_sell'],
                    record['month_sell'],
                    record['day_sell'],
                    record['long_flag'],
                    record['price_buy'],
                    record['price_sell'],
                    record['shares_buy'],
                    record['shares_sell'],
                    record['commission_buy'],
                    record['commission_sell'],
                    record['tax_buy'],
                    record['tax_sell'],
                    record['risk_input'],
                    record['risk_input_percent'],
                    record['risk_initial'],
                    record['risk_initial_percent'],
                    record['risk_actual'],
                    record['risk_actual_percent'],
                    record['stoploss'],
                    record['profit_loss'],
                    record['profit_loss_percent'],
                    record['r_multiple'],
                    record['win_flag'],
                    record['at_work'],
                    record['id_buy'],
                    record['id_sell'],
                    record['from_currency_id'],
                    record['drawdown_id'],
                    record['pool_trading_at_start'],
                    record['active'],
                    record['date_created'],
                    record['date_modified']))
        return result

    def assemble_statement_list_update(self, statements, insupdel=1):
        """
            Creates list of update records from statements,
            that we can use to update at once.
        """
        #NOTE: updating needs more code in the write_to_database function
        return statements.get_statement_list(insupdel) 

    def assemble_statement_list_delete(self, statements, insupdel=2):
        """
            Creates list of from delete statements,
            that we can use to delete at once.
        """
        #NOTE: deleting is not used, because we don't need it.
        # Deleting is done on the table object rows, before pressing execute.
        # When using the app, you need to make sure everything is ok before
        # you press execute.
        return statements.get_statement_list(insupdel)

    def update_stock(self, fields_stock, session, i, finance_id, recordid):
        """
            Add a new stock entry or update an existing one.
        """
        #TODO: figure out what to do with this,
        # after the statement(..., TABLE_NAME) stuff is implemented.
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get stock_name_id from T_STOCK_NAME if it exists (a new entry will be made in T_STOCK_NAME if it doesn't)
            #TODO: add descriptions to market_id_from_market and to
            #stock_name_id_from_stock_name)
            market_id = self.market_id_from_market(fields_stock[i]['market'])
            stock_name_id = self.stock_name_id_from_stock_name(fields_stock[i]['name'], market_id)
            vartax = Decimal(fields_stock[i]['tax'])
            varcommission = Decimal(fields_stock[i]['commission'])
            first_obj = session.query(T_STOCK).filter_by(
                      finance_id=finance_id,
                      price=Decimal(fields_stock[i]['price']),
                      shares=int(fields_stock[i]['shares']),
                      tax=vartax,
                      commission=varcommission
                  ).first()
            if first_obj is None: 
                # NEW
                self.statementStock.add(
                    recordid,
                    T_STOCK(
                        finance_id,
                        stock_name_id,
                        fields_stock[i]['action'],
                        Decimal(fields_stock[i]['price']),
                        int(fields_stock[i]['shares']),
                        vartax,
                        varcommission,
                        0,
                        date_created,
                        date_modified,
                        Decimal(fields_stock[i]['risk'])
                    )
                )
                return True;
        except Exception as ex:
           print(ERROR_UPDATE_STOCK, ex)
        return False;

    def export_records(self, name):
        """
            Return the records from the table or view, defined by name.
        """
        records = None
        session = self.Session()
        try:
            records = session.query(name).all()
        except Exception as ex:
            print("Error in export_records: ", ex)
        finally:
            session.rollback()
            session = None
        return records

    def subcategory_id_from_subcategory(self, subcategory):
        """
            Get the subcategory_id from a subcategory.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get subcategory_id, based on subcategory
            # but first check if the subcategory already exists
            # in T_SUBCATEGORY. If not, add it to the t_sub_categorytable.
            obj = session.query(T_SUBCATEGORY).filter_by(name=subcategory).first() is not None
            if not obj: 
                session.add(T_SUBCATEGORY(subcategory, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_SUBCATEGORY.subcategory_id).label('subcategory_id')):
                    result = instance.subcategory_id
            else:
                for instance in session.query(T_SUBCATEGORY).filter_by(name=subcategory):
                    result = str(instance.subcategory_id)
        except Exception as ex:
            print(ERROR_SUBCATEGORY_ID_FROM_SUBCATEGORY, ex)
        finally:
            session.rollback()
            session = None
        return result

    def account_id_from_account(self, account):
        """
            Get the account_id from an account.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get account id, based on account name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj  = session.query(T_ACCOUNT).filter_by(name=account).first() is not None
            if not obj:
            	#TODO: add the ability to add a market description (Very low priority!)
                session.add(T_ACCOUNT(account, '', date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_ACCOUNT.account_id).label('account_id')):
                    result = instance.account_id
            else:
                for instance in session.query(T_ACCOUNT).filter_by(name=account):
                    result = str(instance.account_id)
        except Exception as ex:
            print(ERROR_ACCOUNT_ID_FROM_ACCOUNT, ex)
        finally:
            session.rollback()
            session = None
        return result

    def category_id_from_category(self, category):
        """
            Get the category_id from a category.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get category_id, based on category name
            # but first check if the category already exists
            # in T_CATEGORY. If not, add it to the t_category table.
            # if category ends with .rx: flg_income = 1, else 0
            if(category[-3:] == '.rx'):
                flg_income = 1
            elif(category[-3:] == '.tx'):
                flg_income = 0
            else:
                raise Exception("Wrong category in input: {0}".format(category))
            obj = session.query(T_CATEGORY).filter_by(name=category).first() is not None
            if not obj: 
                session.add(T_CATEGORY(category, flg_income, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_CATEGORY.category_id).label('category_id')):
                    result = instance.category_id
            else:
                for instance in session.query(T_CATEGORY).filter_by(name=category):
                    result = str(instance.category_id)
        except Exception as ex:
            print("Error retrieving category_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def stock_name_id_from_stock_name(self, stock_name, market_id):
        """
            Get the stock_name_id from T_STOCK_NAME.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get stock_name_id, based on stock_name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_STOCK_NAME).filter_by(name=stock_name, market_id=market_id).first() is not None
            if not obj: 
                session.add(T_STOCK_NAME(stock_name, market_id, '', date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_STOCK_NAME.stock_name_id).label('stock_name_id')):
                    result = instance.stock_name_id
            else:
                for instance in session.query(T_STOCK_NAME).filter_by(name=stock_name, market_id=market_id):
                    result = str(instance.stock_name_id)
        except Exception as ex:
            print("Error retrieving stock_name_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def market_id_from_market(self, code):
        """
            Get the market_id from T_MARKET.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            obj = session.query(T_MARKET).filter_by(code=code).first() is not None
            if not obj: 
                # NOTE: this code means that when new market records have been added
                # during normal usage, a new uninstall/install/import will not be able
                # to fill in the name and country of the market.
                # For now, assume no new ones are added. If there are, add them to the
                # init_tables script!
                #TODO: add extra field in gui for the country code and country name
                # + add this to the input_fields. This way, we can also add new markets.
                # But: perhaps this makes the input too complex and a new button with a dialog window
                # behind it is needed?
                session.add(T_MARKET(None, code, 'TBD', '??', 1, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_MARKET.market_id).label('market_id')):
                    result = instance.market_id
            else:
                for instance in session.query(T_MARKET).filter_by(code=code):
                    result = str(instance.market_id)
        except Exception as ex:
            print("Error retrieving market_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def subcategory_from_subcategory_id(self, subcategory_id):
        """
            Get the subcategory for a given subcategory_id from the T_SUBCATEGORY table.
        """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_SUBCATEGORY).filter_by(subcategory_id=subcategory_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving subcategory from subcategory_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def accountname_from_account_id(self, account_id):
        """
            Get the accountname for a given account_id from the T_ACCOUNT table.
        """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_ACCOUNT).filter_by(account_id=account_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving accountname from account_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def category_from_category_id(self, category_id):
        """
            Get the category for a given category_id from the T_CATEGORY table.
        """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_CATEGORY).filter_by(category_id=category_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving category from category_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result
    
    def currency_id_from_currency(self, currency):
        """
            Get the currency_id from a currency string (e.g.'USD').
        """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_CURRENCY).filter_by(code=currency).first()
            if first_obj is not None:
                result = str(first_obj.currency_id)
            else:
                raise Exception("Error: currency {0} not found! -1 used as a currency_id.".format(currency))
        except Exception as ex:
            print(ERROR_ACCOUNT_ID_FROM_ACCOUNT, ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_formula_id_to_use(self, fields):
        """
            Gets the formula_id to use for a given trading line of the input fields.
        """
        #TODO: determine the rate_id, based on ???
        # Ah no, we need to create a new rate_id,
        # but determine the formula_id to use
        # fields['currency'] = USD => probably the formula with usd
        # fields['category'] = 'trade.tx'
        # fields['subcategory'] =  => 'buy' or 'sell'
        #TODO: do we need to add a dummy formula that multiplies by 1?
        #NOTE: do it manually for now, we'll fix this later
        formula_id = 1
        #if is_a_trade(fields):
        #       if uppercase(fields['currency']) == 'USD':
        #           formula_id = 2 #TODO: was it 2?      
        #       elif somethingsomething:
        #           formula_id = 1
        return formula_id

    def get_latest_rate_id(self):
        """
            Gets the latest rate_id.
        """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_RATE).order_by(T_RATE.rate_id.desc()).first()
            if first_obj is not None:
                result = first_obj.rate_id
            else:
                # We don't have one yet, so by making the last one 0,
                # a get_latest_rate_id() + 1 would become 1
                result = 0
        except Exception as ex:
            print("Error retrieving latest rate_id from T_RATE: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_parameter_value(self, parameter_id):
        """
            Function to get the value that belongs to the given parameter.
        """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_PARAMETER).filter_by(
                    parameter_id=parameter_id):
                result = instance.value
        except Exception as ex:
            print("Error retrieving parameter value: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_currency_exchange_id_from_latest(self):
        """ 
            Gets the first currency_exchange_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            currency_exchange_created = self.get_latest_date_created(TABLE_CURRENCY_EXCHANGE)
            first_obj = session.query(T_CURRENCY_EXCHANGE).filter_by(
                    date_created=currency_exchange_created).first()
            if first_obj is not None:
                result = first_obj.currency_exchange_id
        except Exception as ex:
            print("Error in first_currency_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_rate_id_from_latest(self):
        """ 
            Gets the first rate_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            rate_created = self.get_latest_date_created(TABLE_RATE)
            obj = session.query(T_RATE).filter_by(date_created=rate_created)
            for instance in obj:
                result = instance.rate_id
        except Exception as ex:
            print("Error in first_rate_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_finance_id_from_latest(self):
        """ 
            Gets the first finance_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            finance_created = self.get_latest_date_created(TABLE_FINANCE)
            obj = session.query(T_FINANCE).filter_by(date_created=finance_created)
            for instance in obj:
                result = instance.finance_id
        except Exception as ex:
            print("Error in first_finance_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_latest_date_created(self, tablename):
        """
            Get's the latest date_created value that was added.
        """
        result = current_date()
        session = self.Session()
        try:
            if tablename == TABLE_FINANCE:
                first_obj = session.query(T_FINANCE).order_by(
                    T_FINANCE.finance_id.desc()).first()
            elif tablename == TABLE_RATE:
                first_obj = session.query(T_RATE).order_by(
                    T_RATE.rate_id.desc()).first()
            elif tablename == TABLE_CURRENCY_EXCHANGE:
                first_obj = session.query(T_CURRENCY_EXCHANGE).order_by(
                    T_CURRENCY_EXCHANGE.currency_exchange_id.desc()).first()
            else:
                first_obj = None
            if first_obj is not None:
                result = first_obj.date_created
        except Exception as ex:
            print('Error in get_latest_date_created for table', tablename + ':', ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_finance_record(self, finance_id):
        """ 
            Gets the finance_record with the given finance_id.
        """
        result = []
        session = self.Session()
        try:
            first_obj = session.query(T_FINANCE).filter_by(finance_id =
                    finance_id).first()
            if first_obj is not None:
                result = self.get_record(first_obj)
        except Exception as ex:
            print("Error in get_finance_record: ", ex)
        finally:
            session.rollback()
            session = None
    
    def get_record(self, row):
        """
            Gets a dictionary with the fields of a return record from the
            database.
        """ 
        result = {}
        try:
            #TODO: the call to row_to_dict still gives an error when
            #using both row as self.loaded....
            #TODO: try with row.__tablename__
            result = row_to_dict(row)
        except Exception as ex:
            print("Error in get_record: ", ex)
        return result

    def get_rep_check_total(self, check_totals):
        """
            Returns a string with the totals per account.
        """
        result = "" 
        i = 0
        for entry in check_totals:
            if i == 0:
                result = entry[0] + \
                    '|' + str(entry[1])
            else:
                result = result + ' ' + entry[0] + \
                '|' + str(entry[1])
            i = i + 1
        return result

    def get_rep_check_totals(self):
        """
            Returns a list with the account name and totals.
        """
        values = []
        session = self.Session()
        try:
            obj = session.query(V_REP_CHECK_TOTAL)
            for instance in obj:
                    values.append([instance.account_name,
                        instance.account_total])
        except Exception as ex:
            print("Error in get_rep_check_totals: ", ex)
        finally:
            session.rollback()
            session = None
        return values
    
    def new_drawdown_record(self):
        """
            Creates a new record in T_DRAWDOWN with a default value of 0.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            session.add(T_DRAWDOWN(None, 0, date_created, date_modified))
            session.commit()
            for instance in session.query(
                    func.max(T_DRAWDOWN.drawdown_id).label(
                        'drawdown_id')):
                result = instance.drawdown_id
        except Exception as ex:
            print(ERROR_NEW_DRAWDOWN_RECORD, ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_parameter_commission(self, amount, market):
        """
            Function to determine what parameter to use to select
            the correct commission.
        """
        result = -1
        try:
            #TODO: complete this, to return the correct value for
            #all markets and conditions
            if market == 'ebr' and Decimal(amount) < Decimal(4000) :
                result = 1
            elif market == 'ebr' and Decimal(amount) >= Decimal(4000):
                result = 2
            else:
                result = 1
        except Exception as ex:
            print('Error in get_parameter_commission:', ex)
        return result

    def get_parameter_tax(self, amount, market):
        """
            Function to determine what parameter to use to select
            the correct tax.
        """
        result = -1
        try:
            #TODO: complete this, to return the correct value for
            #all markets and conditions
            if market == 'ebr' and Decimal(amount) < Decimal(4000) :
                result = PARM_TAX
            elif market == 'ebr' and Decimal(amount) >= Decimal(4000):
                result = PARM_TAX
            else:
                result = PARM_TAX
        except Exception as ex:
            print('Error in get_parameter_tax:', ex)
        return result

    def calculate_r_multiple(self, trade_record):
        """ 
            Function to calculate R-multiple.
        """
        #TODO: can be reused for T_INVESTING, so rename trade_record
        # as a parm in all functions that can be reused by T_INVESTING
        # to something more general, like final_record or find another
        # way to reuse this.
        #TODO: make the investment functions the same, also the tables should be the same
        #so we can reuse everything!
        result = DEFAULT_DECIMAL
        try:
            RMunit = trade_record['price_buy'] - trade_record['stoploss']
            result = (trade_record['price_sell'] - trade_record['price_buy'])/RMunit
        except Exception as ex:
            print('Error in calculate_r_multiple:', ex)
        return result

    def get_pool_trading(self):
        """
            Gets the pool available for trading.
        """
        #TODO: problem: when we enter many trades, this wil get whats
        #currently in the pool, not what's in it after the first
        #couple of inserts.
        # - solution: enter trades 1 by 1 + commit every time.
        # - other solution: enter pool value as an input field, which
        #usually requires you to just copy the field values shown at
        #the top and that value could even be filled in by default.
        result = DEFAULT_DECIMAL
        session = self.Session()
        try:
            first_obj = session.query(func.sum(T_FINANCE.amount).label('total')
                    ).filter_by(account_id=TRADING_ACCOUNT_ID).first()
            if first_obj.total is not None:
                result = Decimal(first_obj.total)
            else:
                result = DEFAULT_DECIMAL
        except Exception as ex:
            print("Error in get_pool_trading: ", ex)
        finally:
            session.rollback()
            session = None
        return result

#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""

from decimal import Decimal

TABLE_FINANCE = 't_finance'
TABLE_INVESTMENT = 't_investment'
TABLE_MARKET = 't_market'
TABLE_STOCK_NAME = 't_stock_name'
TABLE_CATEGORY = 't_category'
TABLE_SUBCATEGORY = 't_subcategory'
TABLE_ACCOUNT = 't_account'
TABLE_CURRENCY = 't_currency'
TABLE_CURRENCY_EXCHANGE = 't_currency_exchange'
TABLE_FORMULA = 't_formula'
TABLE_PARAMETER = 't_parameter'
TABLE_TRADE = 't_trade'
TABLE_RATE = 't_rate'
TABLE_DRAWDOWN = 't_drawdown'
TABLE_MARGIN = 't_margin'
TABLE_MARGIN_TYPE = 't_margin_type'
TABLE_POOL = 't_pool'
VIEW_FINANCE = 'v_finance'
VIEW_INVESTMENT = 'v_investment'
VIEW_MARKET = 'v_market'
VIEW_STOCK_NAME = 'v_stock_name'
VIEW_CATEGORY = 'v_category'
VIEW_SUBCATEGORY = 'v_subcategory'
VIEW_ACCOUNT = 'v_account'
VIEW_CURRENCY = 'v_currency'
VIEW_CURRENCY_EXCHANGE = 'v_currency_exchange'
VIEW_FORMULA = 'v_formula'
VIEW_PARAMETER = 'v_parameter'
VIEW_TRADE = 'v_trade'
VIEW_RATE = 'v_rate'
VIEW_DRAWDOWN = 'v_drawdown'
VIEW_MARGIN = 'v_margin'
VIEW_MARGIN_TYPE = 'v_margin_type'
VIEW_POOL = 'v_pool'
VIEW_REP_CHECK_TOTAL = 'v_rep_check_total'

class Error():
    """
        Error messages.
    """
    GET_MARKET_DESCRIPTION = "Error in get_marketdescription: "
    GET_CATEGORIES = "Error in get_categories: "
    GET_ACCOUNTS = "Error in get_accounts: "
    GET_CATEGORIES = "Error in get_categories: "
    GET_SUBCATEGORIES = "Error in get_subcategories: "
    GET_MARKETS = "Error in get_markets: "
    GET_STOCK_NAMES = "Error in get_stocknames: "
    GET_STOCK_DESCRIPTION = "Error in get_stockdescription: "
    GET_STOCK_INFO = "Error in get_stockinfo: "
    GET_CURRENCIES = "Error in get_currencies: "
    EXPORT_RECORDS = "Error in export_records: "
    SUBCATEGORY_ID_FROM_SUBCATEGORY = "Error retrieving subcategory_id: "
    ACCOUNT_ID_FROM_ACCOUNT = "Error retrieving account_id: "
    WRITE_TO_DATABASE_MAIN = "Error in write_to_database from main controller: "
    WRITE_TO_DATABASE = "Error in write_to_database: "
    WRITE_TO_DATABASE_SESSION = "Error creating session in write_to_database: "
    WRITE_TO_DATABASE_CORE = "Error creating session in write_to_database from core_module: "
    INSERT_DATABASE = "Error in write_statement_list_insert: "
    UPDATE_DATABASE = "Error in write_statement_list_update: "
    DELETE_DATABASE = "Error in write_statement_list_delete: "
    GET_INPUT_FIELDS = "Error in get_input_fields: "
    CREATE_STATEMENTS_TABLE_FINANCE = "Error in create_statements_TABLE_FINANCE: "
    CREATE_STATEMENTS_TABLE_STOCK = "Error in create_statements_TABLE_STOCK: "
    CREATE_STATEMENTS_TABLE_TRADE = "Error in create_statements_TABLE_TRADE: "
    CREATE_STATEMENTS_TABLE_INVESTMENT = "Error in create_statements_TABLE_INVESTMENT: "
    CREATE_STATEMENTS_TABLE_RATE = "Error in create_statements_TABLE_RATE: "
    CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE = "Error in create_statements_TABLE_CURRENCY_EXCHANGE: "
    INVADE_ALREADY_STARTED = "Error in invade_already_started: "
    NEW_DRAWDOWN_RECORD = "Error in new_drawdown_record: "
    GET_SPECIFIC_FINANCE_RECORD = "Error in get_specific_finance_record: "

class Message():
    """
       Messages to print to stdout.
    """
    EXEC_ALL = "Executing statements all at once..."
    PREPARING = "Preparing statements..."
    DONE = "Done."
    
class Export():
    """
        Export types.
    """
    LEDGER = "ledger"
    CSV = "csv"
    
DEFAULT_DATE = "1900-01-01"
DEFAULT_DECIMAL = Decimal(0.0)
DEFAULT_INT = 0
TRADING_ACCOUNT_ID = 6
PARM_TAX = 4
STATEMENT_INSERT = 0
STATEMENT_UPDATE = 1
STATEMENT_DELETE = 2

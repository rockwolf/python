BEGIN;

/* drop constraints */
alter table T_FINANCE
    drop constraint fk_subcategory_id;
alter table T_FINANCE
    drop constraint fk_category_id;
alter table T_FINANCE
    drop constraint fk_account_id;
alter table T_RATE
    drop constraint fk_account_id;
alter table T_ACCOUNT
    drop constraint pk_account_id;
alter table T_RATE
    drop constraint fk_market_id;
alter table T_MARKET
    drop constraint pk_market_id;
alter table T_FINANCE
    drop constraint fk_commodity_id;
alter table T_COMMODITY
    drop constraint pk_commidity_id;
alter table T_COMMODITY
    drop constraint fk_market_id;
alter table T_COMMODITY
    drop constraint fk_currency_id;
alter table T_FINANCE
    drop constraint fk_rate_id;
alter table T_RATE
    drop constraint pk_rate_id;
alter table T_RATE
    drop constraint fk_formula_id;
alter table T_CURRENCY_EXCHANGE
    drop constraint fk_finance_id;
alter table T_TRADE
    drop constraint fk_id_buy;
alter table T_TRADE
    drop constraint fk_id_sell;
alter table T_FINANCE
    drop constraint pk_finance_id;
alter table T_INVESTMENT
    drop constraint fk_finance_id;
alter table T_CURRENCY
    drop constraint pk_currency_id;
alter table T_CURRENCY_EXCHANGE
    drop constraint pk_currency_exchange_id;
alter table T_CURRENCY_EXCHANGE
    drop constraint fk_currency_id;
alter table T_DRAWDOWN
    drop constraint pk_drawdown_id;
alter table T_TRADE
    drop constraint pk_trade_id;
alter table T_TRADE
    drop constraint fk_currency_id;
alter table T_TRADE
    drop constraint fk_drawdown_id;

COMMIT;

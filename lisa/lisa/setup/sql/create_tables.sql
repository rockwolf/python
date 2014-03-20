BEGIN;

/* finance */
CREATE TABLE T_ACCOUNT
(
    account_id serial not null,
    name varchar(4000) not null,
    description varchar(4000) not null,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_POOL
(
    pool_id serial not null,
    account_id int not null,
    total decimal(18,6) not null default 0.0,
    invested decimal(18,6) not null default 0.0,
    cash decimal(18,6) not null default 0.0,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_MARKET
(
    market_id int not null,
    code varchar(50) not null,
    name varchar(30) not null,
    country char(3) not null,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique(market_id),
    unique(code)
);

--TODO: add spread col (see t_trade)
CREATE TABLE T_COMMODITY
(
    commodity_id serial not null,
    name varchar(50) not null,
    description varchar(256) not null default '',
    commodity_type_id int not null default 1,
    cfd_general_id int not null default -1,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_COMMODITY_TYPE
(
    commodity_type_id serial not null,
    name varchar(50) not null,
    description varchar(256) not null default '',
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_CFD_GENERAL
(
    cfd_general_id serial not null,
    name varchar(50) not null,
    market_id int not null default -1,
    currency_id int not null default 1,
    tick decimal(18, 6) not null default 1.0,
    tick_value decimal(18, 6) not null default 1.0,
    order_min decimal(18, 6) not null default -1.0,
    order_max decimal(18, 6) not null default -1.0,
    margin_day_proc decimal(18, 6) not null default -1.0,
    margin_night_proc decimal(18, 6) not null default -1.0,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_PARAMETER
(
    parameter_id int not null,
    name varchar(50) not null,
    value varchar(512) not null,
    description varchar(256) not null,
    unique(parameter_id)
);

-- when automatic is checked, the gui should calculate it on the fly.
-- Then, when writing the records to T_RATE, the automatically calculated values
-- should be put in T_RATE.
-- This table thus contains commission and tax values, which might
CREATE TABLE T_RATE
(
    rate_id serial not null,
    commission decimal(18, 6) not null default 0.0,
    tax decimal(18, 6) not null default 0.0,
    automatic_flag int not null default -1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

/* main finance table */
CREATE TABLE T_FINANCE
(
    finance_id serial not null,
    date timestamp not null default '1900-01-01',
    year int not null default 1900,
    month int not null default 1,
    day int not null default 1,
    account_from_id int not null default -1,
    account_to_id int not null default -1,
    amount decimal(18,6) not null default 0.0,
    comment varchar(256) not null default '',
    currency_exchange_id int not null default -1,
    rate_id int not null default -1,
    active int not null default 1, 
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_CURRENCY
(
    currency_id int not null,
    code varchar(3) not null default '',
    description varchar(256) not null default '',
    unique(currency_id)
);

CREATE TABLE T_CURRENCY_EXCHANGE
(
    currency_exchange_id serial not null,
    currency_from_id int not null default -1,
    currency_to_id int not null default -1,
    exchange_rate decimal(18,6) not null default 0.0,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_DRAWDOWN
(
    drawdown_id serial not null,
    drawdown_current int not null default 0,
    drawdown_max int not null default 0,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique(drawdown_id)
);
    
-- TODO: add orig fields and other missing ones, cfr. ods
CREATE TABLE T_TRADE
(
    trade_id serial not null,
    market_id int not null,
    commodity_id int not null,
    date_buy timestamp not null default '1900-01-01',
    year_buy int not null default 1900,
    month_buy int not null default 1,
    day_buy int not null default 1,
    date_sell timestamp not null default '1900-01-01',
    year_sell int not null default 1900,
    month_sell int not null default 1,
    day_sell int not null default 1,
    long_flag int not null default -1,
    price_buy decimal(18,6) not null default 0.0,
    price_buy_orig decimal(18,6) not null default 0.0,
    price_sell decimal(18,6) not null default 0.0,
    price_sell_orig decimal(18,6) not null default 0.0,
    shares_buy int not null default 0,
    shares_sell int not null default 0,
    commission_buy decimal(18,6) not null default 0.0,
    commission_sell decimal(18,6) not null default 0.0,
    tax_buy decimal(18,6) not null default 0.0,
    tax_sell decimal(18,6) not null default 0.0,
    amount_buy decimal(18,6) not null default 0.0,
    amount_sell decimal(18,6) not null default 0.0,
    amount_buy_simple decimal(18,6) not null default 0.0,
    amount_sell_simple decimal(18,6) not null default 0.0,
    risk_input decimal(18,6) not null default 0.0,
    risk_input_percent decimal(18,6) not null default 0.0,
    risk_initial decimal(18,6) not null default 0.0,
    risk_initial_percent decimal(18,6) not null default 0.0,
    risk_actual decimal(18,6) not null default 0.0,
    risk_actual_percent decimal(18,6) not null default 0.0,
    cost_total decimal(18,6) not null default 0.0,
    cost_other decimal(18,6) not null default 0.0,
    stoploss decimal(18,6) not null default 0.0,
    stoploss_orig decimal(18,6) not null default 0.0,
    profit_loss decimal(18,6) not null default 0.0,
    profit_loss_orig decimal(18,6) not null default 0.0,
    profit_loss_total decimal(18,6) not null default 0.0,
    profit_loss_total_percent decimal(18,6) not null default 0.0,
    r_multiple decimal(18,6) not null default 0.0,
    win_flag int not null default -1,
    id_buy int not null default -1,
    id_sell int not null default -1,
    drawdown_id int not null default -1,
    pool_at_start decimal(18,6) not null default 0.0,
    date_expiration timestamp not null default '1900-01-01',
    expired_flag int not null default -1,
    spread decimal(18,6) not null default 0.0,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_VERSION
(
    version_id int not null,
    version varchar(100) not null default '',
    version_info varchar(100) not null default '',
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

COMMIT;

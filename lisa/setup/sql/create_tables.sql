BEGIN;

/* finance */
CREATE TABLE T_SUBCATEGORY
(
    subcategory_id int not null,
    category_id int not null default -1,
    name varchar(20) not null,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_CATEGORY
(
    category_id int not null,
    name varchar(30) not null,
    flg_income int not null,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_ACCOUNT
(
    account_id serial not null,
    name varchar(6) not null,
    description varchar(256) not null default '',
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique(name)
);

CREATE TABLE T_MARKET
(
    market_id int not null,
    code varchar(5) not null,
    name varchar(30) not null,
    country char(3) not null,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique(market_id),
    unique(code)
);

CREATE TABLE T_STOCK_NAME
(
    stock_name_id serial not null,
    name varchar(15) not null,
    market_id int not null default -1,
    description varchar(256) not null default '',
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique (name, market_id)
);

CREATE TABLE T_FORMULA
(
    formula_id int not null,
    value varchar(512) not null,
    description varchar(256) not null,
    unique(formula_id)
);

CREATE TABLE T_PARAMETER
(
    parameter_id int not null,
    name varchar(50) not null,
    value varchar(512) not null,
    description varchar(256) not null,
    unique(parameter_id)
);

-- TODO: when creating records (both trade + finance)
-- you create an entry here, for automatically calculating the commission.
-- create finance record
-- create trade record
-- create rate record
-- update finance record with calculculated commission
-- ?? But should happen in the gui already????
-- extra button to calculate the commission?
-- or on property change of price and shares and amount
--
-- commission and rate are 0? will be calculated here
-- or dependend on checkbox? <= better
-- no checkbox = use those values
-- calculcated = the total
CREATE TABLE T_RATE
(
    rate_id serial not null,
    calculated decimal(18, 6) not null default 0.0,
    calculated_percent decimal(18, 6) not null default 0.0,
    on_shares decimal(18, 6) not null default 0.0,
    on_commission decimal(18, 6) not null default 0.0,
    on_ordersize decimal(18, 6) not null default 0.0,
    on_other decimal(18, 6) not null default 0.0,
    commission decimal(18, 6) not null default 0.0,
    tax decimal(18, 6) not null default 0.0,
    formula_id int not null default -1,
    manual_flag int not null default -1,
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
    account_id int not null default -1,
    category_id int not null default -1,
    subcategory_id int not null default -1,
    amount decimal(18,6) not null default 0.0,
    comment varchar(256) not null default '',
    stock_name_id int not null default -1,
    shares int not null default 0,
    price decimal(18,6) not null default 0.0,
    tax decimal(18,6) not null default 0.0,
    commission decimal (18,6) not null default 0.0,
    active int not null default 1, 
    rate_id int not null default -1,
    currency_exchange_id int not null default -1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_INVESTMENT
(
    --TODO: make something with more info, like T_TRADE
    --TODO: create an extra view, that shows a summary of your current portfolio
    investment_id serial not null,
    stock_name_id int not null default -1,
    action varchar(50) not null,
    price decimal(18,6) not null default 0.0,
    shares int not null default 0,
    tax decimal(18,6) not null default 0.0,
    commission decimal (18,6) not null default 0.0,
    historical decimal(18,6) not null default 0.0,
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
    from_currency_id int not null default -1,
    to_currency_id int not null default -1,
    exchange_rate decimal(18,6) not null default 0.0,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

/* This might belong in bi */
CREATE TABLE T_MARGIN_TYPE
(
    margin_type_id serial not null,
    margin_type varchar(50) not null
);

-- TODO: We need to keep drawdown records... dammit!
-- TODO: create a gui part to maintain this.
-- TODO: when creating trade records, a record needs to be created here too
-- Perhaps maintain this true the position sizing part of the emma app?
CREATE TABLE T_DRAWDOWN
(
    drawdown_id serial not null,
    drawdown_current int not null default 0,
    drawdown_max int not null default 0,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01',
    unique(drawdown_id)
);
    
CREATE TABLE T_TRADE
(
    trade_id serial not null,
    market_id int not null,
    stock_name_id int not null,
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
    price_sell decimal(18,6) not null default 0.0,
    shares_buy int not null default 0,
    shares_sell int not null default 0,
    commission_buy decimal(18,6) not null default 0.0,
    commission_sell decimal(18,6) not null default 0.0,
    tax_buy decimal(18,6) not null default 0.0,
    tax_sell decimal(18,6) not null default 0.0,
    risk_input decimal(18,6) not null default 0.0,
    risk_input_percent decimal(18,6) not null default 0.0,
    risk_initial decimal(18,6) not null default 0.0,
    risk_initial_percent decimal(18,6) not null default 0.0,
    risk_actual decimal(18,6) not null default 0.0,
    risk_actual_percent decimal(18,6) not null default 0.0,
    cost_total decimal(18,6) not null default 0.0,
    stoploss decimal(18,6) not null default 0.0,
    profit_loss decimal(18,6) not null default 0.0,
    profit_loss_percent decimal(18,6) not null default 0.0,
    r_multiple decimal(18,6) not null default 0.0,
    win_flag int not null default -1,
    at_work decimal(18,6) not null default 0.0,
    id_buy int not null default -1,
    id_sell int not null default -1,
    currency_exchange_id int not null default -1,
    drawdown_id int not null default -1,
    pool_trading_at_start decimal(18,6) not null default 0.0,
    active int not null default 1,
    date_created timestamp not null default '1900-01-01',
    date_modified timestamp not null default '1900-01-01'
);

CREATE TABLE T_MARGIN
(
    margin_id serial not null,
    margin_type_id int not null default -1,
    description varchar(100) not null default '',
    value decimal(18,6) not null default 0.0,
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

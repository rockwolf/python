BEGIN;

/* finance */
CREATE TABLE T_SUBCATEGORY
(
    subcategory_id int not null,
    name varchar(20) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_subcategory_id primary key(subcategory_id)
);

CREATE TABLE T_CATEGORY
(
    category_id int not null,
    subcategory_id int not null default 1,
    name varchar(30) not null,
    flg_income int not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_category_id primary key(category_id),
    constraint fk_subcategory_id foreign key(subcategory_id) references T_SUBCATEGORY(subcategory_id)
);

CREATE TABLE T_ACCOUNT
(
    account_id serial not null,
    name varchar(6) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_account_id primary key(account_id)
);

CREATE TABLE T_FINANCE
(
    finance_id serial not null,
    date timestamp not null default current_date,
    year int not null default 0,
    month int not null default 0,
    day int not null default 0,
    account_id int not null,
    category_id int not null,
    subcategory_id int not null,
    amount decimal(18,4) not null default 0.0,
    comment varchar(256) not null default '',
    market_id int not null default 0,
    stock_name_id int not null default 0,
    shares int not null default 0,
    price decimal(18,4) not null default 0.0,
    tax decimal(18,4) not null default 0.0,
    commission decimal (18,4) not null default 0.0,
    reference int not null default 0,
    active int not null default 1, 
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_finance_id primary key(finance_id),
    constraint fk_account_id foreign key(account_id) references T_ACCOUNT,
    constraint fk_category_id foreign key(category_id) references T_CATEGORY,
    constraint fk_subcategory_id foreign key(subcategory_id) references T_SUBCATEGORY,
    constraint fk_market_id foreign key(market_id) references T_MARKET,
    constraint fk_stock_name_id foreign key(stock_name_id) references T_STOCK_NAME
);

/* stock */
CREATE TABLE T_MARKET
(
    market_id int not null,
    code varchar(5) not null,
    name varchar(30) not null,
    country char(3) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_market_id primary key(market_id),
    unique(market_id),
    unique(code)
);

CREATE TABLE T_STOCK_NAME
(
    stock_name_id serial not null,
    name varchar(15) not null,
    market_id int not null,
    description varchar(256) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_stock_name_id primary key(stock_name_id),
    constraint fk_market_id foreign key(market_id) references T_MARKET(market_id),
    unique (name, market_id)
);

CREATE TABLE T_STOCK
(
    stock_id serial not null,
    finance_id int not null,
    stock_name_id int not null,
    action varchar(50) not null,
    price decimal(18,4) not null default 0.0,
    shares int not null default 0,
    tax decimal(18,4) not null default 0.0,
    commission decimal (18,4) not null default 0.0,
    historical decimal(18,4) not null default 0.0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_stock_id primary key(stock_id),
    constraint fk_finance_id foreign key(finance_id) references T_FINANCE(finance_id),
    constraint fk_stock_name_id foreign key(stock_name_id) references T_STOCK_NAME(stock_name_id)
);

CREATE TABLE T_STOCK_CURRENT
(
    code varchar(5) not null,
    name varchar(20) not null,
    shares int not null default 0,
    current_value decimal(18,4) not null default 0.0,
    buy_value decimal(18,4) not null default 0.0,
    amount decimal(18,4) not null default 0.0,
    historical decimal(18,4) not null default 0,
    yield decimal(18,4) not null default 0.0,
    yield_percent decimal(18,4) not null default 0.0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    primary key(code, name)
);

CREATE TABLE T_CURRENCY
(
    currency_id int not null,
    code varchar(3) not null default '',
    description varchar(256) not null default '',
    constraint pk_currency_id primary key(currency_id),
    unique(currency_id)
);

CREATE TABLE T_CURRENCY_EXCHANGE
(
    currency_exchange_id serial not null,
    currency_id int not null,
    exchange_rate decimal(18,6) not null default(1.0),
    finance_id int not null,
    constraint pk_currency_exchange_id primary key(currency_exchange_id),
    constraint fk_currency_id foreign key(currency_id) references T_CURRENCY(currency_id),
    constraint fk_finance_id foreign key(finance_id) references T_FINANCE(finance_id)
);

/* This might belong in bi */
CREATE TABLE T_MARGIN_TYPE
(
    margin_type_id serial not null,
    margin_type varchar(50) not null,
    constraint pk_margin_type_id primary key(margin_type_id)
);

CREATE TABLE T_TRADE
(
    trade_id serial not null,
    date_buy timestamp not null default current_date,
    year_buy int not null default 0,
    month_buy int not null default 0,
    day_buy int not null default 0,
    date_sell timestamp not null default current_date,
    year_sell int not null default 0,
    month_sell int not null default 0,
    day_sell int not null default 0,
    long_flag int not null default 1,
    buy_price decimal(18,4) not null default 0.0,
    sell_price decimal(18,4) not null default 0.0,
    risk decimal(18,4) not null default 0.0,
    initial_risk decimal(18,4) not null default 0.0,
    initial_risk_percent decimal(18,4) not null default 0.0,
    stoploss decimal(18,4) not null default 0.0,
    profit_loss decimal(18,4) not null default 0.0,
    profit_loss_percent decimal(18,4) not null default 0.0,
    win_flag int not null default 1,
    at_work decimal(18,4) not null default 0.0,
    id_buy int not null,
    id_sell int not null,
    currency_id int not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_trade_id primary key(trade_id),
    constraint fk_stock_id foreign key(stock_id) references T_STOCK(stock_id),
    constraint fk_market_id foreign key(market_id) references T_MARKET(market_id),
    constraint fk_id_buy foreign key(id_buy) references T_FINANCE(finance_id),
    constraint fk_id_sell foreign key(id_sell) references T_FINANCE(finance_id),
    constraint fk_currency_id foreign key(currency_id) references T_CURRENCY(currency_id)
);

CREATE TABLE T_RATE
(
    rate_id int not null,
    market_id int not null,
    account_id int not null,
    extra decimal(18, 4) not null default 0.0,
    extra_percent decimal(18, 4) not null default 0.0,
    on_shares decimal(18, 4) not null default 0.0,
    on_commission decimal(18, 4) not null default 0.0,
    finance_id int not null,
    constraint pk_rate_id primary key(rate_id),
    constraint fk_market_id foreign key(market_id) references T_MARKET,
    constraint fk_account_id foreign key(account_id) references T_ACCOUNT(account_id),
    constraint fk_finance_id foreign key(finance_id) references T_FINANCE(finance_id),
    unique(rate_id)
);

CREATE TABLE T_FORMULA
(
    formula_id int not null,
    value varchar(512) not null,
    description varchar(256) not null,
    constraint pk_formula_id primary key(formula_id),
    unique(formula_id)
);

CREATE TABLE T_MARGIN
(
    margin_id serial not null,
    margin_type_id int not null,
    description varchar(100) not null default '',
    value decimal(18,4) not null default 0.0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_smarket_id primary key(margin_id),
    constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(margin_type_id)
);

COMMIT;

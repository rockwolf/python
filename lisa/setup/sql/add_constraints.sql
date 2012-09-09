BEGIN;

/* add constraints */
alter table T_SUBCATEGORY
    add constraint pk_subcategory_id primary key(subcategory_id);
alter table T_CATEGORY
    add constraint pk_category_id primary key(category_id);
alter table T_SUBCATEGORY
    add constraint fk_category_id foreign key(category_id)
    references T_CATEGORY(category_id);
alter table T_ACCOUNT
    add constraint pk_account_id primary key(account_id);
alter table T_MARKET
    add constraint pk_market_id primary key(market_id);
alter table T_STOCK_NAME
    add constraint pk_stock_name_id primary key(stock_name_id);
alter table T_STOCK_NAME
    add constraint fk_market_id foreign key(market_id) references T_MARKET(market_id);
alter table T_FORMULA
    add constraint pk_formula_id primary key(formula_id);
alter table T_RATE
    add constraint pk_rate_id primary key(rate_id);
alter table T_RATE
    add constraint fk_market_id foreign key(market_id) references T_MARKET;
alter table T_RATE
    add constraint fk_account_id foreign key(account_id) references T_ACCOUNT(account_id);
alter table T_RATE
    add constraint fk_formula_id foreign key(formula_id) references T_FORMULA(formula_id);
alter table T_FINANCE
    add constraint pk_finance_id primary key(finance_id);
alter table T_FINANCE
    add constraint fk_account_id foreign key(account_id) references T_ACCOUNT;
alter table T_FINANCE
    add constraint fk_category_id foreign key(category_id) references T_CATEGORY;
alter table T_FINANCE
    add constraint fk_subcategory_id foreign key(subcategory_id) references T_SUBCATEGORY;
alter table T_FINANCE
    add constraint fk_stock_id foreign key(stock_name_id) references T_STOCK_NAME;
alter table T_FINANCE
    add constraint fk_rate_id foreign key(rate_id) references T_RATE;
alter table T_STOCK
    add constraint pk_stock_id primary key(stock_id);
alter table T_STOCK
    add constraint fk_finance_id foreign key(finance_id) references T_FINANCE(finance_id);
alter table T_STOCK
    add constraint fk_stock_name_id foreign key(stock_name_id) references T_STOCK_NAME(stock_name_id);
alter table T_CURRENCY
    add constraint pk_currency_id primary key(currency_id);
alter table T_CURRENCY_EXCHANGE
    add constraint pk_currency_exchange_id primary key(currency_exchange_id);
alter table T_CURRENCY_EXCHANGE
    add constraint fk_currency_id foreign key(currency_id) references T_CURRENCY(currency_id);
alter table T_CURRENCY_EXCHANGE
    add constraint fk_finance_id foreign key(finance_id) references T_FINANCE(finance_id);
alter table T_MARGIN_TYPE
    add constraint pk_margin_type_id primary key(margin_type_id);
alter table T_DRAWDOWN
    add constraint pk_drawdown_id primary key(drawdown_id);
alter table T_TRADE
    add constraint pk_trade_id primary key(trade_id);
alter table T_TRADE
    add constraint fk_id_buy foreign key(id_buy) references T_FINANCE(finance_id);
alter table T_TRADE
    add constraint fk_id_sell foreign key(id_sell) references T_FINANCE(finance_id);
alter table T_TRADE
    add constraint fk_currency_id foreign key(currency_id) references T_CURRENCY(currency_id);
alter table T_TRADE
    add constraint fk_drawdown_id foreign key(drawdown_id) references T_DRAWDOWN(drawdown_id);
alter table T_MARGIN
    add constraint pk_smarket_id primary key(margin_id);
alter table T_MARGIN
    add constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(margin_type_id);

COMMIT;

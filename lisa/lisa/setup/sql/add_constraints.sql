BEGIN;

/* add constraints */
alter table T_ACCOUNT
    add constraint pk_account_id primary key(account_id);
alter table T_MARKET
    add constraint pk_market_id primary key(market_id);
alter table T_COMMODITY
    add constraint pk_commodity_id primary key(commodity_id);
alter table T_COMMODITY
    add constraint fk_market_id foreign key(market_id) references T_MARKET(market_id);
alter table T_COMMODITY
    add constraint fk_currency_id foreign key(currency_id) references T_CURRENCY(currency_id);
alter table T_FORMULA
    add constraint pk_formula_id primary key(formula_id);
alter table T_PARAMETER
    add constraint pk_parameter_id primary key(parameter_id);
alter table T_RATE
    add constraint pk_rate_id primary key(rate_id);
alter table T_RATE
    add constraint fk_formula_id foreign key(formula_id) references T_FORMULA(formula_id);
alter table T_FINANCE
    add constraint pk_finance_id primary key(finance_id);
alter table T_FINANCE
    add constraint fk_account_id foreign key(account_id) references T_ACCOUNT;
alter table T_FINANCE
    add constraint fk_commodity_id foreign key(commodity_id) references T_COMMODITY;
alter table T_FINANCE
    add constraint fk_rate_id foreign key(rate_id) references T_RATE;
alter table T_INVESTMENT
    add constraint pk_investment_id primary key(investment_id);
alter table T_INVESTMENT
    add constraint fk_commodity_id foreign key(commodity_id) references T_COMMODITY(commotidy_id);
alter table T_CURRENCY
    add constraint pk_currency_id primary key(currency_id);
alter table T_CURRENCY_EXCHANGE
    add constraint pk_currency_exchange_id primary key(currency_exchange_id);
alter table T_CURRENCY_EXCHANGE
    add constraint fk_currency_from_id foreign key(currency_from_id) references T_CURRENCY(currency_id);
alter table T_CURRENCY_EXCHANGE
    add constraint fk_currency_to_id foreign key(currency_to_id) references T_CURRENCY(currency_id);
alter table T_FINANCE
    add constraint fk_currency_exchange_id foreign key(currency_exchange_id) references T_CURRENCY_EXCHANGE(currency_exchange_id);
alter table T_MARGIN_TYPE
    add constraint pk_margin_type_id primary key(margin_type_id);
alter table T_DRAWDOWN
    add constraint pk_drawdown_id primary key(drawdown_id);
alter table T_TRADE
    add constraint pk_trade_id primary key(trade_id);
--alter table T_TRADE
--    add constraint fk_id_buy foreign key(id_buy) references T_FINANCE(finance_id);
--alter table T_TRADE
--    add constraint fk_id_sell foreign key(id_sell) references T_FINANCE(finance_id);
alter table T_TRADE
    add constraint fk_currency_exchange_id foreign key(currency_exchange_id) references T_CURRENCY_EXCHANGE(currency_exchange_id);
alter table T_TRADE
    add constraint fk_drawdown_id foreign key(drawdown_id) references T_DRAWDOWN(drawdown_id);
alter table T_MARGIN
    add constraint pk_margin_id primary key(margin_id);
alter table T_MARGIN
    add constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(margin_type_id);
alter table T_POOL
    add constraint fk_account_id foreign key(account_id) references T_ACCOUNT(account_id);
alter table T_BET
    add constraint pk_bet_id primary key(bet_id);

COMMIT;

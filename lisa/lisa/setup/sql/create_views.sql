BEGIN;

/* V_FINANCE */
--DROP VIEW V_FINANCE;
CREATE VIEW V_FINANCE
AS
select
    f.*
from
    t_finance f 
;

/* V_TRADE */
--DROP VIEW V_TRADE;
CREATE VIEW V_TRADE
AS
select
    t.*
from
    t_trade t 
;

/* V_ACCOUNT */
--DROP VIEW V_ACCOUNT;
CREATE VIEW V_ACCOUNT
AS
select
    a.*
from
    t_account a 
;

/* V_RATE */
--DROP VIEW V_RATE;
CREATE VIEW V_RATE
AS
select
    r.*
from
    t_rate r 
;

/* V_CURRENCY */
--DROP VIEW V_CURRENCY;
CREATE VIEW V_CURRENCY
AS
select
    c.*
from
    t_currency c 
;

/* V_CURRENCY_EXCHANGE */
--DROP VIEW V_CURRENCY_EXCHANGE;
CREATE VIEW V_CURRENCY_EXCHANGE
AS
select
    ce.*
from
    t_currency_exchange ce
;

/* V_COMMODITY */
--DROP VIEW V_COMMODITY;
CREATE VIEW V_COMMODITY
AS
select
    sn.*
from
    t_commodity sn
;

/* V_MARKET */
--DROP VIEW V_MARKET;
CREATE VIEW V_MARKET
AS
select
    m.*
from
    t_market m
;

/* V_DRAWDOWN */
--DROP VIEW V_DRAWDOWN;
CREATE VIEW V_DRAWDOWN
AS
select
    d.*
from
    t_drawdown d 
;

/* V_PARAMETER */
--DROP VIEW V_PARAMETER;
CREATE VIEW V_PARAMETER
AS
select
    p.*
from
    t_parameter p 
;

/* V_REP_CHECK_TOTAL */
--DROP VIEW V_REP_CHECK_TOTAL;
CREATE VIEW V_REP_CHECK_TOTAL
AS
select
    *
    --a.name as account_name,
    --sum(f.amount) as account_total
from
    t_finance f
    --inner join t_account a on f.account_id = a.account_id
--group by
--    a.name
;

/* V_POOL */
--DROP VIEW V_POOL;
CREATE VIEW V_POOL
AS
select
    p.*
from
    t_pool p 
;

/* V_ACCOUNT_NAME */
--DROP VIEW V_ACCOUNT_NAME;
CREATE VIEW V_ACCOUNT_NAME
AS
select
    a.account_id as account_id
    , coalesce(a.name || ':', '') as name
from 
    T_ACCOUNT a
where
    a.active = 1
;

/* V_EXPECTANCY */
--DROP VIEW V_EXPECTANCY;
CREATE VIEW V_EXPECTANCY
AS
select
    sum(t.r_multiple)/count(1) as expectancy
from 
    T_TRADE t
where
    t.active = 1
;

/* V_EXPORT_LEDGER */
--DROP VIEW V_EXPORT_LEDGER;
CREATE VIEW V_EXPORT_LEDGER
AS
select
    /*f.date --TODO: format?
    ,f.comment
    ,f.amount_debit
    ,f.amount_credit
    --,c.code
    --TODO: finish */
    *
from
    t_finance f
    --inner join t_currency_exchange ce on ce.currency_exchange_id = f.currency_exchange_id
    --inner join t_currency c on f.currency_id_to = c.currency_id_to
;

/* V_TRADE_JOURNAL */
--DROP VIEW V_TRADE_JOURNAL;
/*CREATE VIEW V_TRADE_JOURNAL
AS
select
    m.name as market
    , c.name as commodity
    , t.date_buy
    , t.date_sell
    , t.long_flag
    , t.price_buy
    , t.price_sell
    , t.shares_buy
    , t.shares_sell
    , t.commission_buy
    , t.commission_sell
    , t.cost_buy
    , t.cost_sell
    , t.risk_input
    , t.risk_initial
    , t.risk_actual
    , t.price_buy_orig
    , t.price_sell_orig
from
    t_trade t
    inner join t_market m on t.market_id = m.market_id
    inner join t_commodity c on t.commodity_id = c.commodity_id
;*/

COMMIT;

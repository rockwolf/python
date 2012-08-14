BEGIN;

/* V_FINANCE */
--DROP VIEW V_FINANCE;
CREATE VIEW V_FINANCE
AS
select
    f.*
from
    t_finance f 

/* V_TRADE */
--DROP VIEW V_TRADE;
CREATE VIEW V_TRADE
AS
select
    t.*
from
    t_trade t 

 /* V_ACCOUNT */
--DROP VIEW V_ACCOUNT;
CREATE VIEW V_ACCOUNT
AS
select
    a.*
from
    t_account a 

/* V_RATE */
--DROP VIEW V_RATE;
CREATE VIEW V_RATE
AS
select
    r.*
from
    t_rate r 

/* V_CURRENCY */
--DROP VIEW V_CURRENCY;
CREATE VIEW V_CURRENCY
AS
select
    c.*
from
    t_currency c 

/* V_CURRENCY_EXCHANGE */
--DROP VIEW V_CURRENCY_EXCHANGE;
CREATE VIEW V_CURRENCY_EXCHANGE
AS
select
    ce.*
from
    t_currency_exchange ce

/* V_STOCK */
--DROP VIEW V_STOCK;
CREATE VIEW V_STOCK
AS
select
    s.*
from
    t_stock s

/* V_STOCK_NAME */
--DROP VIEW V_STOCK_NAME;
CREATE VIEW V_STOCK_NAME
AS
select
    sn.*
from
    t_stock_name sn

/* V_MARKET */
--DROP VIEW V_MARKET;
CREATE VIEW V_MARKET
AS
select
    m.*
from
    t_market m

/* V_CATEGORY */
--DROP VIEW V_CATEGORY;
CREATE VIEW V_CATEGORY
AS
select
    c.*
from
    t_category c

/* V_SUBCATEGORY */
--DROP VIEW V_SUBCATEGORY;
CREATE VIEW V_SUBCATEGORY
AS
select
    sc.*
from
    t_subcategory sc

/* V_STOCK_CURRENT */
--DROP VIEW V_STOCK_CURRENT;
CREATE VIEW V_STOCK_CURRENT
AS
select
    sc.*
from
    t_stock_current sc

/* V_MARGIN */
--DROP VIEW V_MARGIN;
CREATE VIEW V_MARGIN
AS
select
    m.*
from
    t_margin m 

/* V_MARGIN_TYPE */
--DROP VIEW V_MARGIN_TYPE;
CREATE VIEW V_MARGIN_TYPE
AS
select
    mt.*
from
    t_margin_type mt 

/* V_DRAWDOWN */
--DROP VIEW V_DRAWDOWN;
CREATE VIEW V_DRAWDOWN
AS
select
    d.*
from
    t_drawdown d 

/* V_FORMULA */
--DROP VIEW V_FORMULA;
CREATE VIEW V_FORMULA
AS
select
    f.*
from
    t_formula f 

/* V_REP_TRADING_JOURNAL */
--DROP VIEW V_REP_TRADING_JOURNAL;
CREATE VIEW V_REP_TRADING_JOURNAL
AS
with cte_trade_total as
(
    select 
        count(1) as total_records
    from 
        T_TRADE
)
with cte_win_total as
(
    select
        count(1) as total_wins
    from
        T_TRADE
    where
        win_flag = 1
)
with cte_risk_total as
(
    select
        -- TODO: this is only correct if the sell amount is smaller so we
        -- end up more negative then 2%???
        -- TODO: this cte is fucked up. Needs to be fixed.
        f_sell.amount - f_buy.amount
    from
        T_TRADE t
        inner join T_FINANCE f_buy on t.buy_id = f_buy.finance_id
        inner join T_FINANCE f_sell on t.sell_id = f_sell.finance_id
)
with cte_commission_total
(
    select
        f_buy.commission + f_sell.commission as 'commission_total' 
    from
        T_TRADE t
        inner join T_FINANCE f_buy on t.buy_id = f_buy.finance_id
        inner join T_FINANCE f_sell on t.sell_id = f_sell.finance_id
)
select
    t.trade_id,
    t.date_buy,
    t.date_sell,
    t.long_flag,
    t.buy_price,
    t.sell_price,
    t.stock_id,
    t.market_id,
    t.risk,
    t.initial_risk,
    t.initial_risk_percent,
    (select risk_total from cte_risk_total) as 'risk_total'
    t.stoploss,
    t.profit_loss,
    t.profit_loss_percent,
    -- r_multiple = (abs(profit_loss)/total_risked_on_finished_trade)
    abs(t.profit_loss)/(select (buy_price...
    t.win_flag,
    (select total_trades from cte_total_trade)/(select total_wins from cte_total_win)*100 as 'win_percent',
    (select total_wins from cte_total_win) as 'win_sum'
    t.at_work,
    f_buy.comment as 'comment_buy'
    f_sell.comment as 'comment_sell'
    f_buy.commission as 'commission_buy',
    f_sell.commission as 'commission_sell',
    (select commission_total from cte_commission_total) as 'commission_total',
    c.code as 'currency' -- Just for informational purpuses. The values are all displayed in EUR.
from
    T_TRADE t
    inner join T_CURRENCY c on t.currency_id = c.currency_id
    inner join T_FINANCE f_buy on f_buy.finance_id = t.id_buy
    inner join T_FINANCE f_sell on f_sell.finance_id = t.id_sell
    inner join T_STOCK_NAME sn on sn.stock_name_id = t.stock_name_id
    inner join T_MARKET m on m.market_id = t.market_id

COMMIT;

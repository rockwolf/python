BEGIN;

/* V_EXPORT */
--DROP VIEW V_EXPORT;
--TODO: this view needs all the fields to be exported
CREATE VIEW V_EXPORT
AS
select
    f.date,
    c.name as category,
    sc.name as subcategory,
    f.amount,
    f.quantity,
    f.price,
    s.name as stock,
    m.name as market,
    f.tax,
    f.commission,
    f.comment,
    f.risk,
    c.currency,

from
    t_finance f 
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.category_id = c.category_id
        inner join T_SUBCATEGORY sc on c.subcategory_id = sc.subcategory_id
        inner join T_STOCK s on s.stock_id = f.stock_id
        inner join T_MARKET m on m.market_id = f.market_id
        inner join T_CURRENCY cur on cur.currency_id = f.currency_id
        inner join T_CURRENCY_EXCHANGE ce on ce.finance_id = f.finance_id
        --TODO: check if the above is correct and if we indeed have a link
        --from finance_id to the exchange rate. We need it anyway, so add
        --when no longer available.

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
    t.stock_id, -- TODO: make this symbol + market
    t.market_id, --TODO: make this the market name
    t.risk,
    t.initial_risk,
    t.initial_risk_percent,
    '' as 'risk_total'
    t.stoploss,
    t.profit_loss,
    t.profit_loss_percent,
    -- r_multiple = (abs(profit_loss)/total_risked_on_finished_trade)
    abs(t.profit_loss)/(select (buy_price...
    t.win_flag,
    (select total_trades from cte_total_trade)/(select total_wins from cte_total_win)*100 as 'win_percent',
    (select total_wins from cte_total_win) as 'win_sum'
    t.at_work,
    -- TODO: make join with t_finance to show comments for buy and sell
    -- This requires converting row fields to columns.
    f_buy.comment as 'comment_buy'
    f_sell.comment as 'comment_sell'
    (select commission_total from cte_commission_total) as 'commission_total',
    -- TODO: commission_buy, commission_sell => does not need to be
    -- displayed, just the total cost is all we need, but these are needed
    -- to make the calculation
    c.code as 'currency'
from
    T_TRADE t
    inner join T_CURRENCY c on t.currency_id = c.currency_id
    inner join T_FINANCE f_buy on f_buy.finance_id = t.id_buy
    inner join T_FINANCE f_sell on f_sell.finance_id = t.id_sell

COMMIT;

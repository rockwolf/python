BEGIN;

/* V_DRAWDOWN_ACTIVE */
--DROP VIEW V_DRAWDOWN_ACTIVE;
CREATE VIEW V_DRAWDOWN_ACTIVE
AS
select
    a.name as account_name
    ,case
        when t.date_buy = '1900-01-01' then t.date_sell
        else t.date_buy
    end as date_start
    ,t.long_flag
    ,m.code as market_code
    ,sn.name as stock_name
    ,d.drawdown_id
    ,d.drawdown_current
    ,d.drawdown_max
    ,d.date_created
    ,d.date_modified
from
    t_drawdown d
    inner join t_trade t on d.drawdown_id = t.drawdown_id
    inner join t_market m on m.market_id = t.market_id
    inner join t_stock_name sn on sn.stock_name_id = t.stock_name_id
where
    d.active = 1
;

BEGIN;
CREATE VIEW V_TRADING_JOURNAL
AS
select
    t.id,
    t.date,
    p.name as product,
    o.name as object,
    a.name as account
from
    t_finance t
    inner join t_product p on t.pid = p.pid
    inner join t_account a on t.aid = a.aid
    inner join t_object o on t.oid = o.oid
where
    p.pid = 23 or p.pid = 24;

COMMIT;

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

/* V_INVESTMENT */
--DROP VIEW V_INVESTMENT;
CREATE VIEW V_INVESTMENT
AS
select
    s.*
from
    t_investment s
;

/* V_STOCK_NAME */
--DROP VIEW V_STOCK_NAME;
CREATE VIEW V_STOCK_NAME
AS
select
    sn.*
from
    t_stock_name sn
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

/* V_CATEGORY */
--DROP VIEW V_CATEGORY;
CREATE VIEW V_CATEGORY
AS
select
    c.*
from
    t_category c
;

/* V_SUBCATEGORY */
--DROP VIEW V_SUBCATEGORY;
CREATE VIEW V_SUBCATEGORY
AS
select
    sc.*
from
    t_subcategory sc
;

/* V_MARGIN */
--DROP VIEW V_MARGIN;
CREATE VIEW V_MARGIN
AS
select
    m.*
from
    t_margin m 
;

/* V_MARGIN_TYPE */
--DROP VIEW V_MARGIN_TYPE;
CREATE VIEW V_MARGIN_TYPE
AS
select
    mt.*
from
    t_margin_type mt 
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

/* V_FORMULA */
--DROP VIEW V_FORMULA;
CREATE VIEW V_FORMULA
AS
select
    f.*
from
    t_formula f 
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
    a.name as account_name,
    sum(f.amount) as account_total
from
    t_finance f
    inner join t_account a on f.account_id = a.account_id
group by
    a.name
;
--TODO: Integrate this output in mappings_view
--and the gui! After clicking on ADD, you can call the function and update the view.
--Problem: adding does not add it to the db, so get the values in a fuction and add it
--programmatically to a subtotal in code/memory!
COMMIT;

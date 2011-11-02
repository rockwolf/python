BEGIN;
/* finance */
CREATE TABLE T_OBJECT
(
    oid serial not null,
    name varchar(20) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_oid primary key(oid)
);

CREATE TABLE T_PRODUCT
(
    pid serial not null,
    name varchar(30) not null,
    flg_income int not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_pid primary key(pid)
);

CREATE TABLE T_ACCOUNT
(
    aid serial not null,
    name varchar(6) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_aid primary key(aid)
);

create table T_MARGIN_TYPE
(
    mtid serial not null,
    margin_type varchar(50) not null,
    constraint pk_mtid primary key(mtid)
);

CREATE TABLE T_MARGIN
(
    smid serial not null,
    margin_type_id int not null,
    description varchar(100) not null default '',
    value decimal(18,4) not null default 0.0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_smid primary key(smid),
    constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(mtid)
);

CREATE TABLE T_FINANCE
(
    id serial not null,
    date timestamp not null default current_date,
    aid int not null,
    pid int not null,
    oid int not null,
    amount decimal(18,4) not null default 0.0,
    comment varchar(256) not null default '',
    market varchar(256) not null default '',
    stock varchar(256) not null default '',
    shares int not null default 0,
    price decimal(18,4) not null default 0.0,
    tax decimal(18,4) not null default 0.0,
    commission decimal (18,4) not null default 0.0,
    active int not null default 1, 
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_id primary key(id),
    constraint fk_aid foreign key(aid) references T_ACCOUNT,
    constraint fk_pid foreign key(pid) references T_PRODUCT,
    constraint fk_oid foreign key(oid) references T_OBJECT
);

/* stock */
CREATE TABLE T_MARKET
(
    mid serial not null,
    code varchar(5) not null,
    name varchar(30) not null,
    country char(3) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_mid primary key(mid),
    unique (code)
);

CREATE TABLE T_STOCK_NAME
(
    snid serial not null,
    name varchar(15) not null,
    mid int not null,
    description varchar(256) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_snid primary key(snid),
    constraint fk_mid foreign key(mid) references T_MARKET(mid),
    unique (name, mid)
);

CREATE TABLE T_STOCK
(
    sid serial not null,
    id int not null,
    snid int not null,
    action varchar(50) not null,
    price decimal(18,4) not null default 0.0,
    shares int not null default 0,
    tax decimal(18,4) not null default 0.0,
    commission decimal (18,4) not null default 0.0,
    historical decimal(18,4) not null default 0.0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_sid primary key(sid),
    constraint fk_id foreign key(id) references T_FINANCE(id),
    constraint fk_snid foreign key(snid) references T_STOCK_NAME(snid)
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

CREATE TABLE T_TRADE
(
    tid serial not null,
    sid int not null, /* this becomes the link to t_finance: find the sid in T_TRADE (with the correct year and month that's not closed. Otherwise, make another. */
    year int not null default 0,
    month int not null default 0,
    buy_price decimal(18,4) not null default 0.0, /* (buy_price + new buy_price)/2 */
    sell_price decimal(18,4) not null default 0.0, /* (sell_price + new sell_price)/2 */
    stoploss decimal(18,4) not null default 0.0, /* automatically recalculate this */
    shares_total int not null default 0, /* if buy_flg : add shares, if not buy: subtract shares, when 0 => trade closed */
    closed int not null default 0, /* if shares_total becomes zero, this flag will be set to 1 */
    win_flag int not null default 1, /* win_sum not needed, we can get that in a query + it's calc. for/when closed flag = 1 */
    --accuracy decimal(18,4) not null default 0, /* we can get that in a query */
    drawdown int not null default 0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_tid primary key(tid),
    constraint fk_sid foreign key(sid) references T_STOCK(sid)
);

/*
DROP VIEW V_REP_TRADEJOURNAL;
CREATE VIEW V_REP_TRADEJOURNAL
as
select
    t.year,
    t.month,
    t.buy_price,
    t.sell_price,
    t.stoploss,
    t.shares_total,
    t.closed,
    t.win_flag
from
    T_TRADE t
*/
COMMIT;

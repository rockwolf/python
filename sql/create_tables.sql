BEGIN;
/* finance */
CREATE TABLE T_PRODUCT
(
    pid serial not null,
    product varchar(30) not null,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_pid primary key(pid)
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
    description varchar(100),
    value decimal(18,4) not null default 0.0,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_smid primary key(smid),
    constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(mtid)
);
CREATE TABLE T_FINANCE
(
    id serial not null,
    date timestamp,
    acc varchar(6) not null,
    product varchar(50) not null,
    amount decimal(18,4) default 0,
    flag int not null default 0,
    comment varchar(100),
    tags varchar(50),
    date_create timestamp,
    date_modify timestamp,
    constraint pk_id primary key(id)
);
/* bet */
CREATE TABLE T_TEAM
(
    tid serial not null,
    name varchar(30) not null,
    division varchar(30),
    active int not null default 1,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_tid primary key(tid)
);
CREATE TABLE T_BET
(
    bid serial not null,
    id int not null,
    team_a varchar(50) not null,
    team_b varchar(50) not null,
    choice varchar(1) not null,
    pool decimal(18,4) default 0,
    date_create timestamp,
    date_modify timestamp,
    constraint pk_bid primary key(bid),
    constraint fk_id foreign key(id) references T_FINANCE(id)
);
CREATE TABLE T_BET_RESULT
(
    brid serial not null,
    id int not null,
    team_a varchar(50) not null,
    team_b varchar(50) not null,
    choice varchar(1) not null,
    gain decimal(18,4) default 0,
    score_a int default -1,
    score_b int default -1,
    date_create timestamp,
    date_modify timestamp,
    constraint pk_brid primary key(brid),
    constraint fk_id foreign key(id) references T_FINANCE(id)
);
CREATE TABLE T_BET_CURRENT
(
    teamA varchar(50) not null,
    teamB varchar(50) not null,
    date_bet timestamp,
    date_match timestamp,
    pool_total decimal(18,4) default 0,
    date_create timestamp,
    date_modify timestamp,
    primary key(teamA, teamB)
);
/* stock */
CREATE TABLE T_MARKET
(
    mid serial not null,
    code varchar(3) not null,
    name varchar(30) not null,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_mid primary key(mid)
);
CREATE TABLE T_STOCK_NAME
(
    snid serial not null,
    name varchar(10) not null,
    mid int not null,
    description varchar(30),
    date_created timestamp,
    date_modified timestamp,
    constraint pk_snid primary key(snid),
    constraint fk_mid foreign key(mid) references T_MARKET(mid)
);
CREATE TABLE T_STOCK
(
    sid serial not null,
    id int not null,
    snid int not null,
    action varchar(6) not null,
    price decimal(18,4) default 0,
    quantity int default 0,
    historical decimal(18,4) default 0,
    date_create timestamp,
    date_modify timestamp,
    constraint pk_sid primary key(sid),
    constraint fk_id foreign key(id) references T_FINANCE(id),
    constraint fk_snid foreign key(snid) references T_STOCK_NAME(snid)
);
CREATE TABLE T_STOCK_CURRENT
(
    code varchar(5) not null,
    name varchar(20) not null,
    quantity int default 0,
    current_value decimal(18,4) default 0,
    buy_value decimal(18,4) default 0,
    amount decimal(18,4) default 0,
    historical decimal(18,4) default 0,
    yield decimal(18,4) default 0,
    yield_percent decimal(18,4) default 0,
    date_create timestamp,
    date_modify timestamp,
    primary key(code, name)
);
COMMIT;

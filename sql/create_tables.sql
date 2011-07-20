BEGIN;
/* finance */
CREATE TABLE T_OBJECT
(
    oid serial not null,
    name varchar(20) not null,
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
    constraint pk_oid primary key(oid)
);

CREATE TABLE T_PRODUCT
(
    pid serial not null,
    name varchar(30) not null,
    flg_income int not null,
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
    constraint pk_pid primary key(pid)
);

CREATE TABLE T_ACCOUNT
(
    aid serial not null,
    name varchar(6) not null,
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
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
    description varchar(100),
    value decimal(18,4) not null default 0.0,
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
    constraint pk_smid primary key(smid),
    constraint fk_margin_type_id foreign key(margin_type_id) references T_MARGIN_TYPE(mtid)
);

CREATE TABLE T_FINANCE
(
    id serial not null,
    date timestamp default current_date,
    aid int not null,
    pid int not null,
    oid int not null,
    amount decimal(18,4) default 0,
    flag int not null default 0,
    comment varchar(256),
    active int not null default 1, 
    date_create timestamp default current_date,
    date_modify timestamp default current_date,
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
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
    constraint pk_mid primary key(mid),
    unique (code)
);

CREATE TABLE T_STOCK_NAME
(
    snid serial not null,
    name varchar(10) not null,
    mid int not null,
    description varchar(30),
    date_created timestamp default current_date,
    date_modified timestamp default current_date,
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
    price decimal(18,4) default 0,
    quantity int default 0,
    historical decimal(18,4) default 0,
    date_create timestamp default current_date,
    date_modify timestamp default current_date,
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
    date_create timestamp default current_date,
    date_modify timestamp default current_date,
    primary key(code, name)
);
COMMIT;

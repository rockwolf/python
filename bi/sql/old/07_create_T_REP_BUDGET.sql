CREATE TABLE T_REP_BUDGET
(
    bid serial not null,
    acc varchar(6) not null,
    prod varchar(50) not null,
    amount decimal(18,4) default 0,
    initial decimal(18,4) default 0,
    comment varchar(100),
    date_create timestamp,
    date_modify timestamp,
    constraint pk_id primary key(bid)
);

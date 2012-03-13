BEGIN;

/* T_TRADING_JOURNAL */
CREATE TABLE T_TRADING_JOURNAL
(
    tjid serial not null,
    date timestamp not null default current_date,
    sid int not null,
    long_flag char not null default 'L',
    quantity decimal(18,4) not null default 0,
    bought decimal(18,4) not null default 0,
    sold decimal(18,4) not null default 0,
    profit decimal(18,4) not null default 0,
    win int not null default 0,
    win_sum int not null default 0,
    win_proc decimal(18,4) not null default 0,
    processed int not null default 0,
    date_create timestamp not null default current_date,
    date_modify timestamp not null default current_date,
    constraint pk_tjid primary key(tjid),
    constraint fk_sid foreign key(sid) references T_STOCK(sid)
);

COMMIT;

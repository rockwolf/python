BEGIN;

/* T_BUDGET */
-- month values could be used for setting a specific budget for specific months
-- otherwise, the yearly budget/12 will suffice.
CREATE TABLE T_BUDGET
(
    bid int not null,
    bnid int not null,
    bcid int not null,
    counter int not null default 1, -- year (2008, 2009, ...) or month (1, 2, ... 12) counter
    amount decimal(18,4) not null default 0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_bid primary key(bid),
    constraint fk_bnid foreign key(bnid) references T_BUDGET_NAME(bnid),
    constraint fk_bcid foreign key(bcid) references T_BUDGET_CATEGORY(bcid),
    unique(bnid, bcid, counter) -- e.g.: 'standard', 'extra', 2011
);

/* T_BUDGET_NAME */
CREATE TABLE T_BUDGET_NAME
(
    bnid int not null,
    name varchar(50) not null default 'standard',
    name_short varchar(10) not null default 'standard',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_bnid primary key(bnid),
    unique(name),
    unique(name_short)
);

/* T_BUDGET_CATEGORY */
CREATE TABLE T_BUDGET_CATEGORY
(
    bcid int not null,
    name varchar(50) not null,
    name_short varchar(10) not null,
    value decimal(18,4) not null default 0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_budget_id primary key(budget_id),
    unique(name),
    unique(name_short)
);

/* T_REPORT_BUDGET */
CREATE TABLE T_REPORT_BUDGET
(
    rbid serial not null,
    bid int not null default 1,
    amount decimal(18,4) not null default 0,
    comment varchar(100) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_report_budget_id primary key(rbid),
    constraint fk_bid foreign key(bid) references T_BUDGET(bid)
);

/* T_ALLOCATION_CAPITAL */
CREATE TABLE T_ALLOCATION_CAPITAL
(
    acid serial not null,
    allocation_proc decimal(18,4) not null default 0,
    description varchar(100) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_acid primary key(acid)
);

COMMIT;

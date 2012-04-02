BEGIN;

/* T_BUDGET */
CREATE TABLE T_BUDGET
(
    bid int not null,
    bnid int not null,
    bcid int not null,
    year varchar(4) not null,
    amount decimal(18,4) not null default 0,
    constraint pk_bid primary key(bid),
    constraint fk_bnid foreign key(bnid) references T_BUDGET_NAME(bnid),
    constraint fk_bcid foreign key(bcid) references T_BUDGET_CATEGORY(bcid)
);

/* T_BUDGET_NAME */
CREATE TABLE T_BUDGET_NAME
(
    bnid int not null,
    name varchar(50) not null default 'standard',
    name_short varchar(10) not null default 'standard',
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
    constraint pk_budget_id primary key(budget_id),
    unique(name),
    unique(name_short)
);

/* T_REPORT_BUDGET */
CREATE TABLE T_REPORT_BUDGET
(
    rbid serial not null,
    bid int not null default 1,
    bcid int not null,
    year varchar(4) not null,    
    amount decimal(18,4) not null default 0,
    comment varchar(100) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_report_budget_id primary key(rbid),
    constraint fk_bid foreign key(bid) references T_BUDGET(bid),
    constraint fk_bcid foreign key(bcid) references T_BUDGET_CATEGORY(bcid),
    unique(year, bid, bcid)
);

/* T_REPORT_BUDGET_MONTHLY */
CREATE TABLE T_REPORT_BUDGET_MONTHLY
(
    rbmid serial not null,
    bcid int not null,
    year varchar(4) not null,
    month varchar(2) not null,
    amount decimal(18,4) not null default 0,
    comment varchar(100) not null default '',
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_report_budget_monthly_id primary key(rbmid),
    constraint fk_bcid foreign key(bcid) references T_BUDGET_CATEGORY(bcid)
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

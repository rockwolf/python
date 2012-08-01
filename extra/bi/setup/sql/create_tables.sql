BEGIN;

/* T_BUDGET */
CREATE TABLE T_BUDGET
(
    bid serial not null,
    bnid int not null,
    bcid int not null,
    year int not null default 0,
    month in not null default 0,
    amount decimal(18,4) not null default 0,
    active int not null default 0,
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
    bnid serial not null,
    name varchar(50) not null default '',
    name_short varchar(10) not null default '',
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

/* T_PROFILE */
--TODO: check if this table exists at startup of lisa.
--if it does, enable an update button for the profile
--(or even update automatically?)
--This allows for manual manipulation when needed.
-- Note: sometimes you can fill in investing and get values,
-- sometimes you fill in something else and then you get values.
-- This can not be done automatically.
-- Perhaps keep the ods for playing around and just use 80 20 values here?
-- -> YES!
CREATE TABLE T_PROFILE
(
    profile_id int not null,
    defense_percentage decimal(3,2) not null default 0.0,
    offense_percentage decimal(3,2) not null default 0.0,
    investing_percentage decimal(3,2) not null default 0.0,
    cash_percentage decimal(3,2) not null default 0.0,
    trading_percentage decimal(3,2) not null default 0.0,
    constraint pk_profile_id primary key(profile_id)
);
COMMIT;

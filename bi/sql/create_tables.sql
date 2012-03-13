BEGIN;

/* T_BUDGET */
CREATE TABLE T_BUDGET
(
    budget_id int not null,
    budget_name varchar(50) not null default 'standard',
    category_id int not null,
    category_name varchar(50) not null,
    year varchar(4) not null,
    value decimal(18,4) default 0,
    constraint pk_budget_id primary key(budget_id),
    unique(category_id)
);

/* T_REPORT_BUDGET */
CREATE TABLE T_REPORT_BUDGET
(
    bid serial not null,
    category_id int not null,
    year varchar(4) not null,    
    amount decimal(18,4) default 0,
    comment varchar(100),
    date_create timestamp,
    date_modify timestamp,
    constraint pk_report_budget_id primary key(bid),
    constraint fk_category_id foreign key(category_id) references T_BUDGET(category_id)
);

/* T_REPORT_BUDGET_MONTHLY */
CREATE TABLE T_REPORT_BUDGET_MONTHLY
(
    bmid serial not null,
    category_id int not null,
    year varchar(4) not null,
    month varchar(2) not null,
    amount decimal(18,4) default 0,
    comment varchar(100),
    date_create timestamp,
    date_modify timestamp,
    constraint pk_report_budget_id_monthly primary key(bmid),
    constraint fk_category_id_monthly foreign key(category_id) references T_BUDGET(category_id)
);

/* T_ALLOCATION_CAPITAL */
CREATE TABLE T_ALLOCATION_CAPITAL
(
    acid serial not null,
    defense decimal(18,4) not null default 0,
    offense decimal(18,4) not null default 0,
    cash decimal(18,4) not null default 0,
    growth decimal(18,4) not null default 0,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_acid primary key(acid)
);

COMMIT;

BEGIN;

/* T_BUDGET_NAME */
insert into T_BUDGET_NAME(name, name_short, date_created, date_modified)
values('Standard yearly budget', 'yearly', current_date, current_date);

insert into T_BUDGET_NAME(name, name_short, date_created, date_modified)
values('Standard monthly budget', 'monthly', current_date, current_date);

/* T_BUDGET_CATEGORY */
-- perhaps something like this, to utilize the products?
insert into T_BUDGET_CATEGORY(bcid, name, name_short, date_created, date_modified)
values(select pid, substring(name, 0 , len(name) - 4), name from T_PRODUCT);

/* T_BUDGET */
insert into T_BUDGET(bnid, bcid, counter, amount, date_created, date_modified)
values(1, 1, 1, 50.0, current_date, current_date);

/* T_ALLOCATION_CAPITAL */
insert into T_ALLOCATION_CAPITAL(allocation_proc, description, date_created, date_modified)
values(20.0, 'offense - trading', current_date, current_date);

insert into T_ALLOCATION_CAPITAL(allocation_proc, description, date_created, date_modified)
values(80.0, 'defense - dividend', current_date, current_date);

insert into T_ALLOCATION_CAPITAL(allocation_proc, description, date_created, date_modified)
values(0.0, 'spy offense - growth', current_date, current_date);

insert into T_ALLOCATION_CAPITAL(allocation_proc, description, date_created, date_modified)
values(0.0, 'spy defense - cash', current_date, current_date);

commit;
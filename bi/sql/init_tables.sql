BEGIN;

/* T_BUDGET_NAME */
insert into T_BUDGET_NAME(name, name_short, date_created, date_modified)
values('Standard yearly budget', 'yearly', current_date, current_date);

insert into T_BUDGET_NAME(name, name_short, date_created, date_modified)
values('Standard monthly budget', 'monthly', current_date, current_date);

/* T_BUDGET_CATEGORY */
-- perhaps something like this, to utilize the products?
insert into T_BUDGET_CATEGORY(bcid, name, name_short, date_created, date_modified)
values(
    select 
        pid,
        name,
        substring(name, 0 , len(name) - 3)
    from
        T_PRODUCT
    where
        p.flg_income = 0
);

/* T_BUDGET */
-- counter = 1, which means the first month
-- we can select max(counter), so no other months need to be specified
-- if the budget remains the same for all months
insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 2, 1, 0.0, 0, current_date, current_date); -- account

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 4, 1, 0.0, 0, current_date, current_date); -- bet

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 6, 1, 0.0, 1, current_date, current_date); -- bill

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 8, 1, 0.0, 1, current_date, current_date); -- car

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 10, 1, 0.0, 1, current_date, current_date); -- clothes

insert into T_BUDGET(bnid, bcid, counter, amount, date_created, date_modified)
values(1, 12, 1, 50.0, 1, current_date, current_date); -- extra

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 14, 1, 0.0, 1, current_date, current_date); -- food

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 16, 1, 0.0, 1, current_date, current_date); -- gift

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 18, 1, 0.0, 0, current_date, current_date); -- hobby

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 20, 1, 0.0, 0, current_date, current_date); -- house

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 22, 1, 0.0, 0, current_date, current_date); -- invest

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 24, 1, 0.0, 0, current_date, current_date); -- trade

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 26, 1, 0.0, 0, current_date, current_date); -- salary

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 28, 1, 0.0, 0, current_date, current_date); -- tax

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 30, 1, 0.0, 1, current_date, current_date); -- travel

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 32, 1, 0.0, 1, current_date, current_date); -- utilities

insert into T_BUDGET(bnid, bcid, counter, amount, active, date_created, date_modified)
values(1, 34, 1, 0.0, 1, current_date, current_date); -- other

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
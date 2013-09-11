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
-- we can select max, so no other months need to be specified
-- if the budget remains the same for all months
insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 2, 2012, 1, 0.0, 0, current_date, current_date); -- account

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 4, 2012, 1, 0.0, 0, current_date, current_date); -- bet

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 6, 2012, 1, 50.0, 1, current_date, current_date); -- bill

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 8, 2012, 1, 195.83, 1, current_date, current_date); -- car

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 10, 2012, 1, 20.0, 1, current_date, current_date); -- clothes

insert into T_BUDGET(bnid, bcid, year, month, amount, date_created, date_modified)
values(1, 12, 2012, 1, 50.0, 1, current_date, current_date); -- extra

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 14, 2012, 1, 150.0, 1, current_date, current_date); -- food

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 16, 2012, 1, 25.0, 1, current_date, current_date); -- gift

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 18, 2012, 1, 50.0, 1, current_date, current_date); -- hobby

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 20, 2012, 1, 600.0, 1, current_date, current_date); -- house

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 22, 2012, 1, 0.0, 0, current_date, current_date); -- invest

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 24, 2012, 1, 0.0, 0, current_date, current_date); -- trade

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 26, 2012, 1, 0.0, 0, current_date, current_date); -- salary

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 28, 2012, 1, 0.0, 0, current_date, current_date); -- tax

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 30, 2012, 1, 66.67, 1, current_date, current_date); -- travel

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 32, 2012, 1, 150.0, 1, current_date, current_date); -- utilities

insert into T_BUDGET(bnid, bcid, year, month, amount, active, date_created, date_modified)
values(1, 34, 2012, 1, 0.0, 1, current_date, current_date); -- other

/* T_PROFILE */
INSERT INTO T_PROFILE(
    1,
    defense_percentage,
    offense_percentage,
    investing_percentage,
    cash_percentage,
    trading_percentage)
values(80, 20, 80, 20, 100);

commit;

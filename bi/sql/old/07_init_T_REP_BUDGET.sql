BEGIN;

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 500.0, 821.91)
where category ='hobby';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 2350.0, 650.70)
where category = 'car';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 600.0, 578.28)
where category = 'bills';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 0.0, 7.67)
where category = 'tax';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 800.0, 778.00)
where category = 'extra';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 7800, 7650.00)
where category = 'house';

insert into T_REP_BUDGET(year, category, amountset, amountcur)
values(2010, 3600, 0.00)
where category = 'living';

COMMIT;

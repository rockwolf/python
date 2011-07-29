BEGIN;

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(2010, 8400.00, 7800.00)
where category ='house';

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(600.00, 821.91)
where category ='hobby';

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(2600.00, 650.70)
where category = 'car';

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(600.00, 578.28)
where category = 'bills';

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(450.00, 821.91)
where category = 'hobby';

insert into T_REP_BUDGET(year, month, category, amountset, amountcur)
values(600.00, 778.00)
where category = 'extra';

COMMIT;

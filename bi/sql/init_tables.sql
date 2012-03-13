----/*T_REPORT_BUDGET */
--BEGIN;

--/* TODO: Get amountset values from T_REPORT_BUDGET_MONTHLY (x12)
--the monthly budget is the most important one */
--/* 2010 */
--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 7800, 7650.00)
--where category = 'house';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 1800, 0.00)
--where category = 'utilities';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 250.00, 0.00)
--where category = 'clothing';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 1800.00, 0.00)
--where category = 'food';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 2350.00, 650.70)
--where category = 'car';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 600.00, 578.28)
--where category = 'bills';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 500.00, 821.91)
--where category ='hobby';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 0.00, 7.67)
--where category = 'tax';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 778.00)
--where category = 'extra';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 778.00)
--where category = 'gifts';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 0.00)
--where category = 'travel';

--/* 2011 */
--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 7800, 7650.00)
--where category = 'house';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 1000, 0.00)
--where category = 'utilities';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 250.00, 0.00)
--where category = 'clothing';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 1800.00, 0.00)
--where category = 'food';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 2350.00, 650.70)
--where category = 'car';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 600.00, 578.28)
--where category = 'bills';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 500.00, 440)
--where category ='hobby';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 0.00, 0.00)
--where category = 'tax';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 778.00)
--where category = 'extra';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 778.00)
--where category = 'gifts';

--insert into T_REPORT_BUDGET(year, category, amountset, amountcur)
--values(2010, 800.0, 1190.00)
--where category = 'travel';

--COMMIT;

--/* T_REPORT_BUDGET_MONTHLY */
--BEGIN;

--/* TODO: calculate amounts where prod starts with... (prod like '%...') */
--/* maybe TODO: add update statements after the montly inits, to change the budgets per year/month */
--/* house */
--insert into
--	T_REPORT_BUDGET_MONTHLY(year, month, category, amountset, amountcur)
--values(
--	select
--		extract(year from date),
--		extract(month from date),
--        'house',
--        '600',
--        0,
--        0
--	from
--		t_finance
--	group by
--		extract(year from date),
--		extract(month from date)
--	order by date
--);
--/* TODO: don't use values, use the finance table to make it automatic! */
--insert into T_REPORT_BUDGET_MONTHLY(year, month, category, amountset, amountcur)
--/*values(2010, 666.66, 650.00)*/
--values (
--    extract(year from select date),
--    extract(month from select date),
--where category ='house';

--/* house */
--insert into
--	T_REPORT_BUDGET_MONTHLY(year, month, category, amountset, amountcur)
--values(
--	select
--		extract(year from date),
--		extract(month from date),
--        'utilities',
--        '300',
--        0,
--        0
--	from
--		t_finance
--	group by
--		extract(year from date),
--		extract(month from date)
--	order by date
--);
--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(2010, 300, 0.00)
--where categoryid = 'utilities'id;

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(2010, 20.83, 0.00)
--where category = 'clothing';

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(2010, 150, 0.00)
--where category = 'food';

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(600.00, 821.91)
--where category ='hobby';

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(2600.00, 650.70)
--where category = 'car';

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(600.00, 578.28)
--where category = 'bills';

--insert into T_REPORT_BUDGET_MONTHLY(categoryid, year, month, amountset, amountcur)
--values(600.00, 778.00)
--where category = 'extra';

--COMMIT;

--/* T_BUDGET */
--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 1, 'house', 2011, 7800.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 2, 'utilities', 2011, 1800.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 3, 'clothing', 2011, 250.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 4, 'food', 2011, 1800.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 5, 'car', 2011, 2350.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 6, 'bills', 2011, 600.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 7, 'hobby', 2011, 500.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 8, 'tax', 2011, 0.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 9, 'extra', 2011, 600.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 10, 'gifts', 2011, 200.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 11, 'travel', 2011, 800.00);

--insert into T_BUDGET(budget_id, category_id, category_name, year, value)
--values(1, 12, 'health', 2011, 0.00);

--commit;*/
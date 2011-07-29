BEGIN;

/* V_REP_PROGRESSPERYEAR */
CREATE OR REPLACE VIEW V_REP_PROGRESSPERYEAR
as
select
	res.account,
	date_part('year', res.date) as year,
	sum(res.amount)
from
(
	select
		f1.account,
		f1.date,
		case
			when f1.account = 'binb00' and (f1.product <> 'account.rx' and f1.product <> 'invest.refund') then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from T_FINANCE f1
	group by f1.account, f1.date, f1.product, f1.flag, f1.amount
) res
group by res.account,date_part('year', res.date)
order by date_part('year', res.date), res.account;

/* V_REP_PROGRESSPERACCPERMONTH */
CREATE OR REPLACE VIEW V_REP_PROGRESSPERACCPERMONTH
AS
select
    date_part('year', res.date) as year,
	date_part('month', res.date) as month,
	res.account,
	sum(res.amount)
from
(
	select
		f1.account,
		f1.date,
		case
			when f1.account = 'binb00' and f1.product <> 'account.rx' then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from T_FINANCE f1
	group by f1.account, f1.date, f1.product, f1.flag, f1.amount
) res
group by date_part('year', res.date), date_part('month', res.date), res.account
order by date_part('year', res.date), date_part('month', res.date), res.account;

/* V_REP_NETWORTH */
CREATE OR REPLACE VIEW V_REP_NETWORTH
AS
select
    date_part('year', date),
	sum(res.amount) as "Net worth"
from
(
	select
		f1.account,
		f1.date,
		case
			when f1.account = 'binb00' and f1.product <> 'account.rx' then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from T_FINANCE f1
	group by f1.account, f1.date, f1.product, f1.flag, f1.amount
) res
group by date_part('year', date);

/* V_REP_PROGRESSCUMUL */
CREATE OR REPLACE VIEW V_REP_PROGRESSCUMUL
AS
select
	t1.id,
	date_part('year', t1.date),
	t1.amount,
	sum(t1.amount)
from
(
	select
		f1.id,
		f1.account,
		f1.date,
		case
			when f1.account = 'binb00' and (f1.product <> 'account.rx' and f1.product <> 'invest.refund') then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from T_FINANCE f1
	group by f1.id, f1.account, f1.date, f1.product, f1.flag, f1.amount
) t1
join
(
	select
		f1.id,
		f1.account,
		f1.date,
		case
			when f1.account = 'binb00' and (f1.product <> 'account.rx' and f1.product <> 'invest.refund') then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from T_FINANCE f1
	group by f1.id, f1.account, f1.date, f1.product, f1.flag, f1.amount
) t2
on
date_part('year', t2.date) = date_part('year', t1.date) and t2.id <= t1.id
group by date_part('year', t1.date), t1.id, t1.amount
order by date_part('year', t1.date), t1.id;

/* V_REP_CROSSOVER */
CREATE OR REPLACE VIEW V_REP_CROSSOVER
AS
select 
	res.year, res.expenses, res.passive
from
(
	(
		select
			extract(year from t1.date) as year,
			sum(t1.amount) as passive
		from
			T_FINANCE t1
		where
			t1.product = 'invest.dividend'
			or t1.product = 'invest.refund'
		group by
			extract(year from t1.date)
	) a
	join
	(	
		select 
			extract(year from t2.date) as year2,
			sum(t2.amount) as expenses
		from 
			T_FINANCE t2
		where
			t2.flag = 0	
			and t2.product <> 'account.start'
			and t2.product <> 'account.tx'
			and t2.product <> 'invest.invest'
			and t2.product <> 'invest.buystocks'
			and t2.product <> 'invest.changestocks'
			and t2.product <> 'bet.place'
		group by
			extract(year from t2.date)
		order by
			extract(year from t2.date)
	) b
	on a.year = b.year2
) res;

/* V_REP_EXPVSINC */
CREATE OR REPLACE VIEW V_REP_EXPVSINC
AS
select
    vwExpenses.year as year,
    vwExpenses.expenses as expenses,
    vwPassiveIncome.passive as passive,
    vwIncome.income as income,
    vwSalary.salary as salary,
    vwIN.intotal as intotal,
    vwOUT.outtotal as outtotal,
    (vwSalary.salary - vwExpenses.expenses) as savedFromSalary,
    (vwExpenses.expenses/vwSalary.salary)*100 as savedFromSalaryProc,
    (vwIncome.income - vwExpenses.expenses) as savedIncome,
    (vwExpenses.expenses/vwIncome.income)*100 as savedIncomeProc,
    (vwIN.intotal - vwOUT.outtotal) as savedTotal,
    (vwOUT.outtotal/vwIN.intotal)*100 as savedTotalProc
from
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as salary
    from 
        t_finance t1
    where
        t1.flag = 1
        and t1.product = 'salary'
    group by
        extract(year from t1.date)
    order by
        extract(year from t1.date)
) vwSalary
inner join
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as intotal
    from 
        t_finance t1
    where
        t1.flag = 1
    group by
        extract(year from t1.date)
    order by
        extract(year from t1.date)
) vwIN
on vwIN.year = vwSalary.year
inner join
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as outtotal
    from 
        t_finance t1
    where
        t1.flag = 0
    group by
        extract(year from t1.date)
    order by
        extract(year from t1.date)
) vwOUT
on vwOUT.year = vwIN.year
inner join
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as expenses
    from 
        t_finance t1
    where
        t1.flag = 0
        and t1.product <> 'account.start'
        and t1.product <> 'account.tx'
        and t1.product <> 'invest.invest'
        and t1.product <> 'invest.buystocks'
        and t1.product <> 'invest.changestocks'
        and t1.product <> 'bet.place'
    group by
        extract(year from t1.date)
    order by
        extract(year from t1.date)
) vwExpenses
on vwExpenses.year = vwOUT.year
inner join
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as passive
    from
        t_finance t1
    where
        t1.product = 'invest.dividend'
        or t1.product = 'invest.refund'
    group by
        extract(year from t1.date)
) vwPassiveIncome
on vwPassiveIncome.year = vwExpenses.year
inner join
(
    select
        extract(year from t1.date) as year,
        sum(t1.amount) as income
    from
        t_finance t1
    where
        t1.product = 'invest.dividend'
        or t1.product = 'invest.refund'
        or t1.product = 'salary'
        or t1.product = 'stocks.sell'
        or t1.product = 'bets.cashin'
    group by
        extract(year from t1.date)
) vwIncome
on vwIncome.year = vwPassiveIncome.year;

COMMIT;

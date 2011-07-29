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
		a.name as account,
		f.date,
		case
			when a.name = 'binb00' and p.name = 'invest.rx' and o.name = 'dividend' then 0
			else
				case
					when f.flag = 0 then -1*f.amount
					when f.flag = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by a.name, f.date, p.name, f.flag, f.amount
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
		a.name as account,
		f.date,
		case
			when a.name = 'binb00' and p.name = 'invest.rx' and o.name = 'dividend' then 0
			else
				case
					when f.flag = 0 then -1*f.amount
					when f.flag = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by a.name, f.date, p.name, f.flag, f.amount
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
		a.name as account,
		f.date,
        case
            when f.flag = 0 then -1*f.amount
            when f.flag = 1 then f.amount
        end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by a.name, f.date, p.name, f.flag, f.amount
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
		f.id,
		a.name as account,
		f.date,
		case
			when a.name = 'binb00' and p.name = 'invest.rx' and o.name = 'dividend' then 0
			else
				case
					when f.flag = 0 then -1*f.amount
					when f.flag = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by f.id, a.name, f.date, p.name, f.flag, f.amount
) t1
join
(
	select
		f.id,
		f.account,
		f.date,
		case
			when f.account = 'binb00' and p.name = 'invest.rx' and o.name = 'dividend') then 0
			else
				case
					when f.flag = 0 then -1*f.amount
					when f.flag = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by f.id, a.name, f.date, p.name, f.flag, f.amount
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
			extract(year from f.date) as year,
			sum(t1.amount) as passive
		from
			T_FINANCE f 
                inner join T_ACCOUNT a on f.aid = a.aid
                inner join T_PRODUCT p on f.pid = p.pid
                inner join T_OBJECT o on f.oid = o.oid
		where
			p.name = 'invest.rx'
			and (o.name = 'refund' or o.name = 'dividend')
		group by
			extract(year from f.date)
	) a
	join
	(	
		select 
			extract(year from f2.date) as year2,
			sum(f2.amount) as expenses
		from 
			T_FINANCE f2 
                inner join T_ACCOUNT a2 on f2.aid = a2.aid
                inner join T_PRODUCT p2 on f2.pid = p2.pid
                inner join T_OBJECT o2 on f2.oid = o2.oid
		where
			p2.name = 'bill.tx'
			or p2.name = 'car.tx'
			or p2.name = 'clothes.tx'
			or p2.name = 'extra.tx'
			or p2.name = 'food.tx'
			or p2.name = 'gift.tx'
			or p2.name = 'hobby.tx'
			or p2.name = 'house.tx'
			or p2.name = 'invest.tx'
			or p2.name = 'salary.tx'
			or p2.name = 'tax.tx'
			or p2.name = 'travel.tx'
			or p2.name = 'utilities.tx'
			or p2.name = 'other.tx'
		group by
			extract(year from f2.date)
		order by
			extract(year from f2.date)
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
        extract(year from f.date) as year,
        sum(
            case p.flg_income 
                when 1 then f.amount
                else then -1*f.amount
            end
            ) as salary
    from 
        t_finance f 
            inner join t_product p on f.pid = p.pid
    where
        p.name like 'salary%'
    group by
        extract(year from f.date)
    order by
        extract(year from f.date)
) vwSalary
inner join
(
    select
        extract(year from f.date) as year,
        sum(f.amount) as intotal
    from 
        t_finance f
    where
        p.flg_income = 1
    group by
        extract(year from f.date)
    order by
        extract(year from f.date)
) vwIN
on vwIN.year = vwSalary.year
inner join
(
    select
        extract(year from f.date) as year,
        sum(f.amount) as outtotal
    from 
        t_finance f
    where
        f.flag = 0
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

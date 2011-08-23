BEGIN;

/* NOTE: Create or replace view... is bugged! Using drop view in stead. */
/* V_REP_PROGRESSPERYEAR */
DROP VIEW V_REP_PROGRESSPERYEAR;
CREATE VIEW V_REP_PROGRESSPERYEAR
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
					when p.flg_income = 0 then -1*f.amount
					when p.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by a.name, f.date, p.name, o.name, p.flg_income, f.amount
) res
group by res.account, date_part('year', res.date)
order by date_part('year', res.date), res.account;

/* V_REP_PROGRESSPERACCPERMONTH */
DROP VIEW V_REP_PROGRESSPERACCPERMONTH;
CREATE VIEW V_REP_PROGRESSPERACCPERMONTH
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
					when p.flg_income = 0 then -1*f.amount
					when p.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by a.name, f.date, p.name, o.name, p.flg_income, f.amount
) res
group by date_part('year', res.date), date_part('month', res.date), res.account
order by date_part('year', res.date), date_part('month', res.date), res.account;

/* V_REP_NETWORTH */
DROP VIEW V_REP_NETWORTH;
CREATE VIEW V_REP_NETWORTH
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
            when p.flg_income = 0 then -1*f.amount
            when p.flg_income = 1 then f.amount
        end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
    where
        p.name like 'account%'
        or p.name = 'invest.tx'
	group by a.name, f.date, p.name, p.flg_income, f.amount
) res
group by date_part('year', date);

/* V_REP_PROGRESSCUMUL */
DROP VIEW V_REP_PROGRESSCUMUL;
CREATE VIEW V_REP_PROGRESSCUMUL
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
					when p.flg_income = 0 then -1*f.amount
					when p.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by f.id, a.name, f.date, p.name, o.name, p.flg_income, f.amount
) t1
join
(
	select
		f.id,
		a.name as account,
		f.date,
		case
			when a.name = 'binb00' and p.name = 'invest.rx' and o.name = 'dividend' then 0
			else
				case
					when p.flg_income = 0 then -1*f.amount
					when p.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
        inner join T_OBJECT o on f.oid = o.oid
	group by f.id, a.name, f.date, p.name, o.name, p.flg_income, f.amount
) t2
on
date_part('year', t2.date) = date_part('year', t1.date) and t2.id <= t1.id
group by date_part('year', t1.date), t1.id, t1.amount
order by date_part('year', t1.date), t1.id;

/* V_REP_CROSSOVER */
DROP VIEW V_REP_CROSSOVER;
CREATE VIEW V_REP_CROSSOVER
AS
select 
	res.year, res.expenses, res.passive
from
(
	(
		select
			extract(year from f.date) as year,
			sum(f.amount) as passive
		from
			T_FINANCE f 
                inner join T_ACCOUNT a on f.aid = a.aid
                inner join T_PRODUCT p on f.pid = p.pid
                inner join T_OBJECT o on f.oid = o.oid
		where
			p.name = 'invest.rx'
			and (o.name = 'refund' or o.name = 'dividend')
            or p.name = 'bill.rx'
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
DROP VIEW V_REP_EXPVSINC;
CREATE VIEW V_REP_EXPVSINC
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
    (
        case 
            when (vwIN.intotal - vwOUT.outtotal)/vwIN.intotal*100 < 0 then  0
            else (vwIN.intotal - vwOUT.outtotal)/vwIN.intotal*100
        end
    ) as savedTotalProc
from
(
    select
        extract(year from f.date) as year,
        sum(
            case p.flg_income 
                when 1 then f.amount
                else -1*f.amount
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
            inner join t_product p on f.pid = p.pid
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
            inner join t_product p on f.pid = p.pid
    where
        p.flg_income = 0
    group by
        extract(year from f.date)
    order by
        extract(year from f.date)
) vwOUT
on vwOUT.year = vwIN.year
inner join
(
    select
        extract(year from f.date) as year,
        sum(f.amount) as expenses
    from 
        t_finance f
            inner join t_product p on f.pid = p.pid
    where
        p.name = 'bill.tx'
        or p.name = 'car.tx'
        or p.name = 'clothes.tx'
        or p.name = 'extra.tx'
        or p.name = 'food.tx'
        or p.name = 'gift.tx'
        or p.name = 'hobby.tx'
        or p.name = 'house.tx'
        or p.name = 'salary.tx'
        or p.name = 'tax.tx'
        or p.name = 'travel.tx'
        or p.name = 'utilities.tx'
        or p.name = 'other.tx'
    group by
        extract(year from f.date)
    order by
        extract(year from f.date)
) vwExpenses
on vwExpenses.year = vwOUT.year
inner join
(
    select
        extract(year from f.date) as year,
        sum(f.amount) as passive
    from
        t_finance f 
            inner join T_ACCOUNT a on f.aid = a.aid
            inner join T_PRODUCT p on f.pid = p.pid
            inner join T_OBJECT o on f.oid = o.oid
    where
        p.name = 'invest.rx'
        and (o.name = 'refund' or o.name = 'dividend')
        or p.name = 'bill.rx'
    group by
        extract(year from f.date)
) vwPassiveIncome
on vwPassiveIncome.year = vwExpenses.year
inner join
(
    select
        extract(year from f.date) as year,
        sum(
            case p.flg_income
                when 1 then f.amount
                else -1*f.amount
            end
            ) as income
    from
        t_finance f 
            inner join T_ACCOUNT a on f.aid = a.aid
            inner join T_PRODUCT p on f.pid = p.pid
            inner join T_OBJECT o on f.oid = o.oid
    where
        p.name = 'invest.rx'
        and (o.name <> 'refund' and o.name <> 'dividend')
        or p.name like 'salary%'
        or p.name like 'bet%'
    group by
        extract(year from f.date)
) vwIncome
on vwIncome.year = vwPassiveIncome.year;

/* V_REP_CHECK */
DROP VIEW V_REP_CHECK;
CREATE VIEW V_REP_CHECK
AS
select
    a.name as account,
    sum(
        case p.flg_income
            when 1 then f.amount
            else -1*f.amount
        end
    ) as total 
from
    t_finance f 
        inner join T_ACCOUNT a on f.aid = a.aid
        inner join T_PRODUCT p on f.pid = p.pid
group by a.name
order by a.name;

/* V_REP_EXPENSESPERPRODUCT */
DROP VIEW V_REP_EXPENSESPERPRODUCT;
CREATE VIEW V_REP_EXPENSESPERPRODUCT
AS
select
    subq.*
from
(
    select 
        /*extract(year from f.date) as year,*/
        y.year,
        substring(p.name, 1, char_length(p.name)-3) as product,
        sum(coalesce(f.amount, 0)) as expenses 
    from
    (   
        (select distinct extract(year from f.date) as year from t_finance f) as x
        cross join t_product
        /*cross join (select aid, name as account from t_account) as acc*/
    ) as y
    left outer join t_finance f on y.year = extract(year from f.date) and y.pid = f.pid
    inner join t_product p on p.pid = y.pid
    /*inner join T_ACCOUNT a on a.aid = y.aid*/
    where 
        p.flg_income = 0
        /*and a.name <> 'binb00'*/
        /*and f.aid <> 4*/
        and p.name <> 'account.tx'
        and p.name <> 'invest.tx'
    group by
        y.year, p.name
        /*extract(year from f.date), p.name*/
) subq;

COMMIT;

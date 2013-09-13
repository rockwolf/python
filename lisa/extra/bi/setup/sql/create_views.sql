BEGIN;

/* NOTE: Create or replace view... is bugged! Using drop view in stead. */
/* V_REP_PROGRESSPERYEAR */
--DROP VIEW V_REP_PROGRESSPERYEAR;
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
	    when f.account_id = 4 and f.category_id = 21 and f.subcategory_id = 6 then 0
	    else
                case
		    when c.flg_income = 0 then -1*f.amount
		    when c.flg_income = 1 then f.amount
	        end
	end as amount
    from T_FINANCE f
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.category_id = c.category_id
        inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
	group by a.name, f.date, c.name, sc.name, c.flg_income, f.amount
) res
group by res.account, date_part('year', res.date)
order by date_part('year', res.date), res.account;

/* V_REP_PROGRESSPERACCPERMONTH */
--DROP VIEW V_REP_PROGRESSPERACCPERMONTH;
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
			when f.account_id = 4 and f.category_id = 21 and f.subcategory_id = 6 then 0
			else
				case
					when c.flg_income = 0 then -1*f.amount
					when c.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.category_id = c.category_id
        inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
	group by a.name, f.date, c.name, sc.name, c.flg_income, f.amount
) res
group by date_part('year', res.date), date_part('month', res.date), res.account
order by date_part('year', res.date), date_part('month', res.date), res.account;

/* V_REP_NETWORTH */
--DROP VIEW V_REP_NETWORTH;
CREATE VIEW V_REP_NETWORTH;
AS
select
    date_part('year', f.date),
    sum(f.amount) as "Net worth"
from T_FINANCE f
    inner join T_ACCOUNT a on f.account_id = a.account_id
where
    a.account_id <> 5 -- betting account not counted
group by date_part('year', res.date);

/* V_REP_PROGRESSCUMUL */
--DROP VIEW V_REP_PROGRESSCUMUL;
CREATE VIEW V_REP_PROGRESSCUMUL
AS
select
    t1.finance_id,
    date_part('year', t1.date),
    t1.amount,
    sum(t1.amount)
from
(
    select
		f.finance_id,
		a.name as account,
		f.date,
		case
			when f.account_id = 4 and f.category_id = 21 and f.subcategory_id = 6 then 0
			else
				case
					when c.flg_income = 0 then -1*f.amount
					when c.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.subcategory_id = c.subcategory_id
        inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
	group by f.finance_id, a.name, f.date, c.name, sc.name, c.flg_income, f.amount
) t1
join
(
	select
		f.finance_id,
		a.name as account,
		f.date,
		case
			when f.account_id = 4 and f.category_id = 21 and f.subcategory_id = 6 then 0
			else
				case
					when c.flg_income = 0 then -1*f.amount
					when c.flg_income = 1 then f.amount
				end
		end as amount
	from T_FINANCE f
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.category_id = c.category_id
        inner join T_SUBCATEGORY_ID sc on f.subcategory_id = sc.subcategory_id
	group by f.finance_id, a.name, f.date, c.name, sc.name, c.flg_income, f.amount
) t2
on
date_part('year', t2.date) = date_part('year', t1.date) and t2.finance_id <= t1.finance_id
group by date_part('year', t1.date), t1.finance_id, t1.amount
order by date_part('year', t1.date), t1.finance_id;

/* V_REP_CROSSOVER */
--DROP VIEW V_REP_CROSSOVER;
CREATE VIEW V_REP_CROSSOVER
AS
select 
	res.year, res.expenses, res.passive
from
(
    (	
        select 
            extract(year from f.date) as year,
	    sum(f.amount) as expenses
	from 
            T_FINANCE f 
            inner join T_ACCOUNT a on f.account_id = a.account_id
            inner join T_CATEGORY c on f.category_id = c.category_id
            inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
        where
	    f.category_id in (
                6 --'bill.tx'
	        ,8 --'car.tx'
	        ,10 --'clothes.tx'
	        ,12 --'extra.tx'
	        ,14 --'food.tx'
	        ,16 --'gift.tx'
	        ,18 --'hobby.tx'
	        ,20 --'house.tx'
	        ,26 --'salary.tx'
	        ,28 --'tax.tx'
	        ,30 --'travel.tx'
	        ,32 --'utilities.tx'
	        ,34 --'other.tx'
        )
	group by
	    extract(year from f.date)
	order by
	    extract(year from f.date)
	) a
	left join
	(
		select
			extract(year from f2.date) as year2,
			sum(f2.amount) as passive
		from
			T_FINANCE f2 
                inner join T_ACCOUNT a2 on f2.account_id = a2.account_id
                inner join T_CATEGORY c2 on f2.category_id = c2.category_id
                inner join T_SUBCATEGORY sc2 on f2.subcategory_id = sc2.subcategory_id
		where
			f2.category_id = 21
			and f2.subcategory_id = 6
		group by
			extract(year from f2.date)
	) b
	on a.year = b.year2
) res;

/* V_REP_EXPVSINC */
--DROP VIEW V_REP_EXPVSINC;
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
    (
        case 
            when (100 - vwExpenses.expenses/vwSalary.salary*100) < 0 then  0
            else (100 - vwExpenses.expenses/vwSalary.salary*100)
        end
    )  as savedFromSalaryProc,
    (vwIncome.income - vwExpenses.expenses) as savedIncome,
    (
        case 
            when (100 - vwExpenses.expenses/vwIncome.income*100) < 0 then  0
            else (100 - vwExpenses.expenses/vwIncome.income*100)
        end
    ) as savedIncomeProc,
    (vwIN.intotal - vwOUT.outtotal) as savedTotal,
    (
        case 
            when (100 - vwOUT.outtotal/vwIN.intotal*100) < 0 then  0
            else (100 - vwOUT.outtotal/vwIN.intotal*100)
        end
    ) as savedTotalProc
from
(
    select
        extract(year from f.date) as year,
        sum(
            case c.flg_income 
                when 1 then f.amount
                else -1*f.amount
            end
            ) as salary
    from 
        t_finance f 
            inner join t_category c on f.category_id = c.category_id
    where
        f.pid in (25,26)
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
            inner join t_category c on f.category_id = c.category_id
    where
        c.flg_income = 1
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
            inner join t_category c on f.category_id = c.category_id
    where
        c.flg_income = 0
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
            inner join t_category c on f.pid = c.category_id
    where
        f.pid in (
            6 --'bill.tx'
	    ,8 --'car.tx'
	    ,10 --'clothes.tx'
	    ,12 --'extra.tx'
	    ,14 --'food.tx'
	    ,16 --'gift.tx'
	    ,18 --'hobby.tx'
	    ,20 --'house.tx'
	    ,26 --'salary.tx'
	    ,28 --'tax.tx'
	    ,30 --'travel.tx'
	    ,32 --'utilities.tx'
	    ,34 --'other.tx'
        )
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
            inner join T_ACCOUNT a on f.account_id = a.account_id
            inner join T_CATEGORY c on f.category_id = c.category_id
            inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
    where
        (f.category_id = 21
        and f.subcategory_id in (5, 6))
        or f.category_id = 5 -- TODO: doublecheck these conditions!
    group by
        extract(year from f.date)
) vwPassiveIncome
on vwPassiveIncome.year = vwExpenses.year
inner join
(
    select
        extract(year from f.date) as year,
        sum(
            case c.flg_income
                when 1 then f.amount
                else -1*f.amount
            end
            ) as income
    from
        t_finance f 
            inner join T_ACCOUNT a on f.account_id = a.account_id
            inner join T_CATEGORY c on f.category_id = c.category_id
            inner join T_SUBCATEGORY sc on f.subcategory_id = sc.subcategory_id
    where
        f.category_id = 21
        and (c.subcategory_id <> 5 and c.subcategory_id <> 6)
        or f.category_id in (3,4,25,26) --bet% and salary% -- TODO: doublecheck everything!
    group by
        extract(year from f.date)
) vwIncome
on vwIncome.year = vwPassiveIncome.year;

/* V_REP_EXPENSESPERPRODUCT */
--DROP VIEW V_REP_EXPENSESPERPRODUCT;
CREATE VIEW V_REP_EXPENSESPERPRODUCT
AS
select 
    y.year,
    substring(c.name, 1, char_length(c.name)-3) as category, --TODO: change product in the report to category
    sum(coalesce(f.amount, 0)) as expenses 
from
    (   
       (select distinct extract(year from f.date) as year from t_finance f) as x
       cross join t_category
    ) as y
    left join t_finance f on y.year = extract(year from f.date)
        and y.category_id = f.category_id
    inner join t_category c on c.category_id = y.category_id
where 
    c.flg_income = 0
        and f.category_id <> 2
        and f.category_id <> 22
    group by
        y.year, c.name

/* TODO: put this in tj and finish the calculations. */
/* V_REP_TRADING_JOURNAL */
--DROP VIEW V_REP_TRADING_JOURNAL;
CREATE VIEW V_REP_TRADING_JOURNAL
AS
select
    t.id,
    t.date,
    p.name as product,
    o.name as object,
    a.name as account
from
    t_finance t
    inner join t_product p on t.pid = p.pid
    inner join t_account a on t.aid = a.aid
    inner join t_object o on t.oid = o.oid
where
    p.pid = 23 or p.pid = 24;

/* V_REP_PROFILE */
--DROP VIEW V_REP_PROFILE;
CREATE VIEW V_REP_PROFILE
AS
select
    'dummy_defense' as defense,
    'dummy_offense' as offense,
    'dummy_defense_investing' as investing,
    'dummy_defense_cash' as cash,
    'dummy_offense_trading' as trading
    /* something like this:
    select
    sum(f.amount) as pool,
    sum(f.amount)/(select allocation_proc from T_ALLOCATION_CAPITAL where acid = 1) as offense,
    sum(f.amount) - sum(f.amount)/(select allocation_proc from T_ALLOCATION_CAPITAL where acid = 2) as defense
from 
    t_finance f
where
    f.category_id = 1
    and f.account_id = 4;*/
from
    t_finance f 
        inner join T_ACCOUNT a on f.account_id = a.account_id
        inner join T_CATEGORY c on f.category_id = c.category_id

COMMIT;

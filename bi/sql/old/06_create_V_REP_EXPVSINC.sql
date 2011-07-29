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
        and t1.prod = 'salary'
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
        and t1.prod <> 'account.start'
        and t1.prod <> 'account.tx'
        and t1.prod <> 'invest.invest'
        and t1.prod <> 'invest.buystocks'
        and t1.prod <> 'invest.changestocks'
        and t1.prod <> 'bet.place'
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
        t1.prod = 'invest.dividend'
        or t1.prod = 'invest.refund'
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
        t1.prod = 'invest.dividend'
        or t1.prod = 'invest.refund'
        or t1.prod = 'salary'
        or t1.prod = 'stocks.sell'
        or t1.prod = 'bets.cashin'
    group by
        extract(year from t1.date)
) vwIncome
on vwIncome.year = vwPassiveIncome.year

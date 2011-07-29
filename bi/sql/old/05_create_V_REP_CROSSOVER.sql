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
			t1.prod = 'invest.dividend'
			or t1.prod = 'invest.refund'
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
			and t2.prod <> 'account.start'
			and t2.prod <> 'account.tx'
			and t2.prod <> 'invest.invest'
			and t2.prod <> 'invest.buystocks'
			and t2.prod <> 'invest.changestocks'
			and t2.prod <> 'bet.place'
		group by
			extract(year from t2.date)
		order by
			extract(year from t2.date)
	) b
	on a.year = b.year2
) res

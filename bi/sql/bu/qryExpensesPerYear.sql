select 
	extract(year from t1.date) as year,
	sum(t1.amount) as amount
from 
	finance t1
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
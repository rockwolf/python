select
	extract(year from t1.date) as year,
	sum(t1.amount) as passive
from
	finance t1
where
	t1.prod = 'invest.dividend'
	or t1.prod = 'invest.refund'
group by
	extract(year from t1.date)
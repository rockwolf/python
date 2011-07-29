select
	res.acc,
	date_part('year', res.date) as year,
	sum(res.amount)
from
(
	select
		f1.acc,
		f1.date,
		case
			when f1.flag = 0 then -1*f1.amount
			when f1.flag = 1 then f1.amount
		end as amount
	from finance f1
	where
		f1.acc = 'dexb00'
	group by f1.acc, f1.date, f1.prod, f1.flag, f1.amount
) res
group by res.acc, date_part('year', res.date)
order by date_part('year', res.date),res.acc;
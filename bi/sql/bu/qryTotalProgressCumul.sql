select
	t1.id,
	date_part('year', t1.date),
	t1.amount,
	sum(t1.amount)
from
(
	select
		f1.id,
		f1.acc,
		f1.date,
		case
			when f1.acc = 'binb00' and (f1.prod <> 'account.rx' and f1.prod <> 'invest.refund') then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from finance f1
	group by f1.id, f1.acc, f1.date, f1.prod, f1.flag, f1.amount
) t1
join
(
	select
		f1.id,
		f1.acc,
		f1.date,
		case
			when f1.acc = 'binb00' and (f1.prod <> 'account.rx' and f1.prod <> 'invest.refund') then 0
			else
				case
					when f1.flag = 0 then -1*f1.amount
					when f1.flag = 1 then f1.amount
				end
		end as amount
	from finance f1
	group by f1.id, f1.acc, f1.date, f1.prod, f1.flag, f1.amount
) t2
on
date_part('year', t2.date) = date_part('year', t1.date) and t2.id <= t1.id
group by date_part('year', t1.date), t1.id, t1.amount
order by date_part('year', t1.date), t1.id;
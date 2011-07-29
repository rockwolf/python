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
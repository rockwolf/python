select sum(amount) as car from t_finance where prod like 'car%' and date between '2010-01-01' and '2010-12-31';
select sum(amount) as bill from t_finance where prod like 'bill%' and date between '2010-01-01' and '2010-12-31';
select sum(amount) as hobby from t_finance where prod like 'hobby%' and date between '2010-01-01' and '2010-12-31';
select sum(amount) as extra from t_finance where prod like 'extra%' and date between '2010-01-01' and '2010-12-31';
select sum(amount) as house from t_finance where prod like 'house%' and date between '2010-01-01' and '2010-12-31';

select sum(amount) as living from t_finance where prod like 'living%' and date between '2010-01-01' and '2010-12-31';

/* Author: rockwolf
 * Date: 2012-07-31
 * Function: Adds year, month and day values to T_FINANCE,
 * for easy searching and comparing of dates, without having
 * to deal with a time component.
 */
alter table t_finance add year int not null default 0;
alter table t_finance add month int not null default 0;
alter table t_finance add day int not null default 0;
update t_finance set year = (select EXTRACT(YEAR from date) from t_finance);
update t_finance set month = (select EXTRACT(MONTH from date) from t_finance);
update t_finance set day = (select EXTRACT(DAY from date) from t_finance);

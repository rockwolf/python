/* Author: rockwolf
 * Date: 2012-07-31
 * Function: Adds year, month and day values to T_TRADE,
 * for easy searching and comparing of dates, without having
 * to deal with a time component.
 */
alter table t_stock drop year;
alter table t_stock drop month;
alter table t_stock add year_buy int not null default 0;
alter table t_stock add month_buy int not null default 0;
alter table t_stock add day_buy int not null default 0;
alter table t_stock add year_sell int not null default 0;
alter table t_stock add month_sell int not null default 0;
alter table t_stock add day_sell int not null default 0;
update t_stock set year_buy = EXTRACT(YEAR from date_buy);
update t_stock set month_buy = EXTRACT(MONTH from date_buy);
update t_stock set day_buy = EXTRACT(DAY from date_buy);
update t_stock set year_sell = EXTRACT(YEAR from date_sell);
update t_stock set month_sell = EXTRACT(MONTH from date_sell);
update t_stock set day_sell = EXTRACT(DAY from date_sell);

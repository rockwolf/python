-- 2012-03-18: add risk column
alter table t_finance add risk numeric(18, 4) not null default 0.0;
alter table t_stock add risk numeric(18, 4) not null default 0.0;

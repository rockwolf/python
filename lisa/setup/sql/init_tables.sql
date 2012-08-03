BEGIN;
/* accounts */
INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('dexb00', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('dexb01', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('dexb02', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('binb00', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('unib00', current_date, current_date);

/* markets */
INSERT INTO T_MARKET(code, name, country, date_created, date_modified)
values('ams', 'Amsterdam', 'NL', current_date, current_date);

INSERT INTO T_MARKET(code, name, country, date_created, date_modified)
values('ebr', 'Brussels', 'BE', current_date, current_date);

INSERT INTO T_MARKET(code, name, country, date_created, date_modified)
values('etr', 'Xetra', 'DE', current_date, current_date);

INSERT INTO T_MARKET(code, name, country, date_created, date_modified)
values('epa', 'Paris', 'FR', current_date, current_date);

INSERT INTO T_MARKET(code, name, country, date_created, date_modified)
values('other', 'Other', '', current_date, current_date);

/* stock names */
INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('rhji', '2', 'RHJI International', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('nests', '2', 'Nestle', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('devg', '2', 'Devgen', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('enin', '2', '4 Energy Invest', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('adhof', '1', 'Koninklijke AHOLD N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('dexb', '2', 'Dexia', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('crxl', '1', 'Crucell N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('drak', '1', 'Draka Holding N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('theb', '2', 'Thenergo N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('eurn', '2', 'Euronav', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('tnet', '2', 'Telenet', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('exm', '2', 'Exmar', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('cofb', '2', 'Cofinimmo N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('fme', '3', 'Fresenius Medical Care', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('gsz', '4', 'GDF Suez SA', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('zsl23.90', '2', 'Zilver Sprinter Long 23.90', current_date, current_date);

/* t_category */
--TODO: gather all product combinations and put them in here.
--it's no longer sufficient to put in bill.rx for example,
--we need:
--bill.rx None
--bill.rx mutuality
--bill.rx police
--...
--and also check other combo's
INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'account.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'account.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'bet.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'bet.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'car.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'car.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'clothes.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'clothes.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'extra.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'extra.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'food.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'food.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'gift.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'gift.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'hobby.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'hobby.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'house.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'house.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'salary.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'salary.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'tax.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'tax.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'travel.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'travel.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'utilities.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'utilities.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'other.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(scid, name, flg_income, date_created, date_modified)
values(1, 'other.tx', 0, current_date, current_date);

/* t_subcategory */
INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('none', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('buystocks', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('sellstocks', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('invest', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('refund', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('dividend', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('close', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('electricity', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('gas', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('water', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('mutuality', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('internet', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('dexia', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('other', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('insurance', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('police', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('vik', current_date, current_date);

INSERT INTO T_SUBCATEGORY(name, date_created, date_modified)
values('phone', current_date, current_date);

/* margin types */
INSERT INTO T_MARGIN_TYPE(margin_type)
values('safety');

/* margins */
/* -- Note: this might belong to the bi sql folder
INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve after crossover', 1600000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safety margin passive income', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safe withdrawal rate', 0.03, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Bargain reserve', 100000, current_date, current_date);*/
COMMIT;

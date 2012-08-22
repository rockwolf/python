BEGIN;
/* accounts */
INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('belf00', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('belf01', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('belf02', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('binb00', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('unib00', current_date, current_date);

INSERT INTO T_ACCOUNT(name, date_created, date_modified)
values('whsi00', current_date, current_date);

/* markets */
INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(1, 'ams', 'Amsterdam', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(2, 'ebr', 'Brussels', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(3, 'etr', 'Xetra', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(4, 'epa', 'Paris', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(5, 'other', 'Other', '', 1, current_date, current_date);

--TODO: enter market names for commodities here
INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(6, 'gbp', 'London', '', 1, current_date, current_date);

/* stock names */
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('rhji', 2, 'RHJI International', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('nests', 2, 'Nestle', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('devg', 2, 'Devgen', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('enin', 2, '4 Energy Invest', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('adhof', 1, 'Koninklijke AHOLD N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('dexb', 2, 'Dexia', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('crxl', 1, 'Crucell N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('drak', 1, 'Draka Holding N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('theb', 2, 'Thenergo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('eurn', 2, 'Euronav', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('tnet', 2, 'Telenet', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('exm', 2, 'Exmar', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('cofb', 2, 'Cofinimmo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('fme', 3, 'Fresenius Medical Care', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('gsz', 4, 'GDF Suez SA', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('zsl23.90', 2, 'Zilver Sprinter Long 23.90', 1, current_date, current_date);

--TODO: figure out the markets to which each commodity belongs.
--TODO: enter commodity descriptions
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CFI2Z2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CFI2Z3.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('NGU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('NGV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.GOLD.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.MGOLD.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.MSILVER.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.SILVER.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('GCV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HGU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HGZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('MINISIU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('MINISIZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PAU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PAZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PLV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SIU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SIZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.BRENT.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.WTI.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CLV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CLX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HOU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HOV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCOV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCOX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LGOU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LGOV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CCZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CTV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CTZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('KCZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCCU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LEV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LSUV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LWBX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SBV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZCU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZCZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLV2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSX2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWU2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWZ2.cfd', 6, 'London Brent Oil', 1, current_date, current_date);

/* t_subcategory */
INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(1, 'none', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(2, 'buy', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(3, 'sell', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(4, 'invest', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(5, 'refund', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(6, 'dividend', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(7, 'close', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(8, 'electricity', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(9, 'gas', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(10, 'water', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(11, 'mutuality', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(12, 'internet', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(13, 'belfius', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(14, 'insurance', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(15, 'police', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(16, 'vik', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(17, 'phone', current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, name, date_created, date_modified)
values(18, 'other', current_date, current_date);

/* t_category */
--TODO: gather all product combinations and put them in here.
--it's no longer sufficient to put in bill.rx for example,
--we need:
--bill.rx None
--bill.rx mutuality
--bill.rx police
--...
--and also check other combo's
INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(1, 1, 'account.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(2, 1, 'account.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(3, 1, 'bet.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(4, 1, 'bet.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(5, 8, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(6, 8, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(7, 9, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(8, 9, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(9, 10, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(10, 10, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(11, 11, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(12, 11, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(13, 12, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(14, 12, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(15, 13, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(16, 13, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(17, 14, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(18, 14, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(19, 15, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(20, 15, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(21, 16, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(22, 16, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(23, 17, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(24, 17, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(25, 18, 'bill.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(26, 18, 'bill.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(27, 1, 'car.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(28, 1, 'car.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(29, 1, 'clothes.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(30, 1, 'clothes.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(31, 1, 'extra.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(32, 1, 'extra.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(33, 1, 'food.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(34, 1, 'food.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(35, 1, 'gift.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(36, 1, 'gift.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(37, 1, 'hobby.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(38, 1, 'hobby.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(39, 1, 'house.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(40, 1, 'house.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(41, 2, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(42, 2, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(43, 3, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(44, 3, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(45, 4, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(46, 4, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(47, 5, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(48, 5, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(49, 6, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(50, 6, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(51, 7, 'invest.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(52, 7, 'invest.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(53, 2, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(54, 2, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(55, 3, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(56, 3, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(57, 5, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(58, 5, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(59, 6, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(60, 6, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(61, 18, 'trade.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(62, 18, 'trade.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(63, 1, 'salary.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(64, 1, 'salary.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(65, 1, 'tax.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(66, 1, 'tax.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(67, 1, 'travel.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(68, 1, 'travel.tx', 0, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(69, 1, 'other.rx', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, subcategory_id, name, flg_income, date_created, date_modified)
values(70, 1, 'other.tx', 0, current_date, current_date);

/* currencies */
INSERT INTO T_CURRENCY(currency_id, code, description)
values(1, 'EUR', 'Euro');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(2, 'USD', 'United States Dollar');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(3, 'CHF', 'Swiss Frank');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(4, 'CAD', 'Canadian Dollar');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(5, 'JPY', 'Japanese Yen');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(6, 'NZD', 'New Zealand Dollar');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(7, 'AUD', 'Australian Dollar');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(8, 'GBP', 'British Pound');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(9, 'HKD', 'Hong Kong Dollar');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(10, 'DKK', 'Danish Krone');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(11, 'PLN', 'Polish Zloty');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(12, 'MXN', 'Mexican Peso');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(13, 'SEK', 'Swedish Krona');

INSERT INTO T_CURRENCY(currency_id, code, description)
values(14, 'RUB', 'Russian Ruble');

/* t_formula */
INSERT INTO T_FORMULA(formula_id, value, description)
values(1, '%d0+%d1*%d2', 'WHS commission calculation for US markets: <solid amount>+<small fraction>*<number of shares>.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(2, '%d0+%d1*%d2/100', 'WHS commission calculation for non-US markets: <solid amount>+<small percentage>*<order size>.');

/* t_margin_types */
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

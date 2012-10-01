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

/* t_category */
INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(1, 'account.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(2, 'account.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(3, 'bet.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(4, 'bet.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(5, 'bill.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(6, 'bill.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(7, 'car.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(8, 'car.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(9, 'clothes.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(10, 'clothes.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(11, 'extra.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(12, 'extra.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(13, 'food.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(14, 'food.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(15, 'gift.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(16, 'gift.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(17, 'hobby.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(18, 'hobby.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(19, 'house.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(20, 'house.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(21, 'invest.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(22, 'invest.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(23, 'trade.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(24, 'trade.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(25, 'salary.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(26, 'salary.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(27, 'tax.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(28, 'tax.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(29, 'travel.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(30, 'travel.tx', 0, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(31, 'other.rx', 1, 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, flg_income, active, date_created, date_modified)
values(32, 'other.tx', 0, 1, current_date, current_date);

/* t_subcategory */
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(1, 1, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(2, 1, 'buy', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(3, 1, 'sell', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(4, 1, 'invest', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(5, 1, 'refund', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(6, 1, 'dividend', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(7, 1, 'close', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(8, 1, 'electricity', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(9, 1, 'gas', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(10, 1, 'water', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(11, 1, 'mutuality', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(12, 1, 'internet', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(13, 1, 'belfius', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(14, 1, 'insurance', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(15, 1, 'police', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(16, 1, 'vik', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(17, 1, 'phone', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(18, 1, 'other', 1, current_date, current_date);

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
--TODO: add a column where you can say what the parameters are?
--TODO: add a table which contains the values for tax and commissions?
INSERT INTO T_FORMULA(formula_id, value, description)
values(1, '{0}+{1}*{2}', 'WHS commission calculation for US markets: <solid amount>+<small fraction>*<number of shares>.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(2, '{0}+{1}*{2}/100', 'WHS commission calculation for non-US markets: <solid amount>+<small percentage>*<order size>.');

/* t_parameter */
INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(1, 'parm01', 9.75, 'Commission binkbank for buying regular stocks.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(2, 'parm02', 7.25, 'Commission binkbank for buying regular stocks < 2500 EUR.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(3, 'parm03', 0.25, 'Solid amount for calculation of costs for commodities on US markets.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(4, 'parm04', 0.0022, 'Tax on Belgian stock market transactions.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(5, 'parm05', 0.25, 'dividend tax - BE');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(6, 'parm06', 0.2675, 'dividend tax - D');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(7, 'parm07', 0.30, 'dividend tax - FR');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(8, 'parm08', 0.15, 'dividend tax - NL');

/* t_margin_types */
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

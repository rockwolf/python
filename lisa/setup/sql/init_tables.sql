BEGIN;
/* accounts */
INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('belf00', 'Checking account', current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('belf01', 'Savings account', current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('belf02', 'Retirement savings', current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('binb00', 'Investing account', current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('unib00', 'Betting account', current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, date_created, date_modified)
values('whsi00', 'Trading account', current_date, current_date);

/* markets */
-- NOTE: see list of country codes at:
-- http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm
--TODO: check if this still maps to the current market id's in production
--and check this when using KETTLE
INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(1, 4, '', '', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(2, 4, 'ams', 'Amsterdam stock exchange AEX25', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(3, 4, 'ebr', 'Brussels stock exchange BEL20', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(4, 4, 'etr', 'Frankfurt Xetra DAX30', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(5, 4, 'epa', 'Paris Stock Exchange CAC40', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(6, 4, 'other', 'Other', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(7, 4, 'eli', 'Lisbon Stock Exchange', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(8, 4, 'lse', 'London Stock Exchange', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(9, 4, 'ise', 'Irish Stock Exchange (Dublin)', 'IE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(10, 4, 'mil', 'Milan Stock Exchange', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(11, 4, 'bma', 'Bolsa de Madrid', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(12, 4, 'vse', 'Vienna Stock Exchange', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(13, 6, 'cfd .gold', 'CFD - World Spot Gold', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(14, 6, 'cfd .silver', 'CFD - World Spot Silver', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(15, 6, 'cfd oil', 'CFD - Brent and WTI oil', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(16, 6, 'cfd other non-share', 'CFD - other non-share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(17, 6, 'cfd BE', 'CFD - Belgium', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(18, 6, 'cfd FR', 'CFD - France', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(19, 6, 'cfd DE', 'CFD - Germany', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(20, 6, 'cfd UK', 'CFD - United Kingdom', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(21, 6, 'cfd DK', 'CFD - Denmark', 'DK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(22, 6, 'cfd FI', 'CFD - Finland', 'FI', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(23, 6, 'cfd IT', 'CFD - Italy', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(24, 6, 'cfd NL', 'CFD - Netherlands', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(25, 6, 'cfd NO', 'CFD - Norway', 'NO', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(26, 6, 'cfd PT', 'CFD - Portugal', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(27, 6, 'cfd SE', 'CFD - Sweden', 'SE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(28, 6, 'cfd CH', 'CFD - Switzerland', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(29, 6, 'cfd ES', 'CFD - Spain', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(30, 6, 'cfd other share', 'CFD - other share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(31, 6, 'cfd AU', 'CFD - Australia', 'AU', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(32, 6, 'cfd AT', 'CFD - Austria', 'AT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(33, 6, 'cfd CN', 'CFD - China', 'CN', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(34, 6, 'cfd PL', 'CFD - Poland', 'PL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(35, 6, 'cfd SG', 'CFD - Singapore', 'SG', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(36, 4, 'nyse', 'Ney York Stock Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(37, 4, 'nasdaq', 'Nasdaq', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(38, 4, 'otc bb & pinksheets', 'OTC BB & pinksheets', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(39, 4, 'amex', 'American Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, account_id, code, name, country, active, date_created, date_modified)
values(40, 4, 'other us', 'Other US markets', 'US', 1, current_date, current_date);

/* stock names */
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('', 1, '', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('rhji', 3, 'RHJI International', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('nests', 3, 'Nestle', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('devg', 3, 'Devgen', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('enin', 3, '4 Energy Invest', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('adhof', 2, 'Koninklijke AHOLD N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('dexb', 3, 'Dexia', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('crxl', 2, 'Crucell N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('drak', 2, 'Draka Holding N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('theb', 3, 'Thenergo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('eurn', 3, 'Euronav', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('tnet', 3, 'Telenet', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('exm', 3, 'Exmar', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('cofb', 3, 'Cofinimmo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('fme', 4, 'Fresenius Medical Care', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('gsz', 5, 'GDF Suez SA', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('zsl23.90', 3, 'Zilver Sprinter Long 23.90', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('car', 5, 'Carrefour', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('boka', 2, 'Koninklijke Boskalis Westminster NV', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('sr', 2, 'SNS Reaal NV', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('solb', 3, 'Solvay S.A.', 1, current_date, current_date);

--TODO: figure out the markets to which each commodity belongs.
--TODO: enter commodity descriptions
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CFI2Z2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CFI2Z3.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('NGU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('NGV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.GOLD.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.MGOLD.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.MSILVER.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.SILVER.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('GCV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HGU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HGZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('MINISIU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('MINISIZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PAU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PAZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('PLV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SIU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SIZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.BRENT.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('.WTI.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CLV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CLX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HOU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('HOV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCOV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCOX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LGOU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LGOV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CCZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CTV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CTZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('KCZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCCU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LEV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LSUV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LWBX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SBV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZCU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZCZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLV2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSX2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWU2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWZ2.cfd', 7, 'London Brent Oil', 1, current_date, current_date);

/* t_category */
--TODO: only 1 category, use a negative amount to know if it's rx or tx!
INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(1, 'account', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(2, 'bet', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(3, 'bill', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(4, 'car', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(5, 'clothes', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(6, 'extra', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(7, 'food', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(8, 'gift', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(9, 'hobby', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(10, 'house', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(11, 'invest', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(12, 'trade', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(13, 'salary', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(14, 'tax', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(15, 'travel', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(16, 'utilities', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(17, 'other', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(18, 'health', 1, current_date, current_date);

INSERT INTO T_CATEGORY(category_id, name, active, date_created, date_modified)
values(19, 'cash', 1, current_date, current_date);

/* t_category_type */
--TODO: add the category ids!
INSERT INTO T_CATEGORY_TYPE(category_type_id, category_id, name, active, date_created, date_modified)
values(1, 'prepaid_expenses', 1, current_date, current_date);

INSERT INTO T_CATEGORY_TYPE(category_type_id, category_id, name, active, date_created, date_modified)
values(2, 'prepaid_income', 1, current_date, current_date);

INSERT INTO T_CATEGORY_TYPE(category_type_id, category_id, name, active, date_created, date_modified)
values(3, 'accounts_payable', 1, current_date, current_date);

INSERT INTO T_CATEGORY_TYPE(category_type_id, category_id, name, active, date_created, date_modified)
values(4, 'accounts_receivable', 1, current_date, current_date);

/* t_subcategory */
-- none
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(1, 1, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(2, 2, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(3, 3, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(4, 4, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(5, 5, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(6, 6, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(7, 7, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(8, 8, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(9, 9, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(10, 10, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(11, 11, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(12, 12, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(13, 13, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(14, 14, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(15, 15, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(16, 16, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(17, 17, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(18, 18, 'none', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(19, 19, 'none', 1, current_date, current_date);

-- buy
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(20, 11, 'buy', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(21, 12, 'buy', 1, current_date, current_date);

-- sell
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(22, 11, 'sell', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(23, 12, 'sell', 1, current_date, current_date);

-- invest
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(24, 11, 'invest', 1, current_date, current_date);

-- refund
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(25, 11, 'refund', 1, current_date, current_date);

-- dividend
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(26, 11, 'dividend', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(27, 12, 'dividend', 1, current_date, current_date);

-- close
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(28, 11, 'close', 1, current_date, current_date);

-- electricity
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(29, 16, 'electricity', 1, current_date, current_date);

-- gas
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(30, 16, 'gas', 1, current_date, current_date);

-- water
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(31, 16, 'water', 1, current_date, current_date);

-- mutuality
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(32, 3, 'mutuality', 1, current_date, current_date);

-- internet
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(33, 3, 'internet', 1, current_date, current_date);

-- belfius
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(34, 3, 'belfius', 1, current_date, current_date);

-- other
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(35, 9, 'other', 1, current_date, current_date);

-- insurance
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(36, 4, 'insurance', 1, current_date, current_date);

INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(37, 10, 'insurance', 1, current_date, current_date);

-- police
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(38, 3, 'police', 1, current_date, current_date);

-- vik
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(39, 3, 'vik', 1, current_date, current_date);

-- phone
INSERT INTO T_SUBCATEGORY(subcategory_id, category_id, name, active, date_created, date_modified)
values(40, 3, 'phone', 1, current_date, current_date);

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
values(1, '{0}', 'Default: no formula needed, just use the value.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(2, '{0}+{1}*{2}', 'WHS commission calculation for US markets: <solid amount>+<small fraction>*<number of shares>.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(3, '{0}+{1}*{2}/100', 'WHS commission calculation for non-US markets: <solid amount>+<small percentage>*<order size>.');

--TODO: this system is under review.
--Might be too complex to implement.
INSERT INTO T_FORMULA(formula_id, value, description)
values(4, 'if {0} >= {1} : {2} else {3}', 'commission be stocks');

INSERT INTO T_FORMULA(formula_id, value, description)
values(5, '','commission us stocks');

/* t_rate */
INSERT INTO T_RATE(calculated, calculated_percent, on_shares, on_commission, on_ordersize, on_other, commission, tax, formula_id, automatic_flag, date_created, date_modified)
values(-1.0, -1.0/100, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1, 0, current_date, current_date);

/* t_parameter */
INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(1, 'comm_binb_be', 9.75, 'Commission binkbank for buying regular stocks.');

--TODO: add another parameter for the 2500 EUR!
--We need to check for this in the code that determines
--which formula/parameter to use.
INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(2, 'comm_binb_be_below2500', 7.25, 'Commission binkbank for buying regular stocks < 2500 EUR.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(3, 'comm_whsi_commodities_us', 0.25, 'Solid amount for calculation of costs for commodities on US markets.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(4, 'tax_stocks_be', 0.0025, 'Tax on Belgian stock market transactions.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(5, 'tax_dividend_be', 0.25, 'dividend tax - BE');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(6, 'tax_dividend_d', 0.2675, 'dividend tax - D');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(7, 'tax_dividend_fr', 0.30, 'dividend tax - FR');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(8, 'tax_dividend_nl', 0.15, 'dividend tax - NL');

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

/* t_version */
INSERT INTO T_VERSION
values(1, '2.0', 'Lisa with trading options.', current_date, current_date);

COMMIT;

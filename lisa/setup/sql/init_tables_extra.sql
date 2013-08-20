-- Add market names
-- NOTE: see list of country codes at:
-- http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm
--TODO: check if this still maps to the current market id's in production
--and check this when using KETTLE
INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(2, 'ams', 'Amsterdam stock exchange AEX25', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(3, 'ebr', 'Brussels stock exchange BEL20', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(4, 'etr', 'Frankfurt Xetra DAX30', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(5, 'epa', 'Paris Stock Exchange CAC40', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(6, 'other', 'Other', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(7, 'eli', 'Lisbon Stock Exchange', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(8, 'lse', 'London Stock Exchange', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(9, 'ise', 'Irish Stock Exchange (Dublin)', 'IE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(10, 'mil', 'Milan Stock Exchange', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(11, 'bma', 'Bolsa de Madrid', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(12, 'vse', 'Vienna Stock Exchange', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(13, 'cfd .gold', 'CFD - World Spot Gold', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(14, 'cfd .silver', 'CFD - World Spot Silver', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(15, 'cfd oil', 'CFD - Brent and WTI oil', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(16, 'cfd other non-share', 'CFD - other non-share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(17, 'cfd BE', 'CFD - Belgium', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(18, 'cfd FR', 'CFD - France', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(19, 'cfd DE', 'CFD - Germany', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(20, 'cfd UK', 'CFD - United Kingdom', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(21, 'cfd DK', 'CFD - Denmark', 'DK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(22, 'cfd FI', 'CFD - Finland', 'FI', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(23, 'cfd IT', 'CFD - Italy', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(24, 'cfd NL', 'CFD - Netherlands', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(25, 'cfd NO', 'CFD - Norway', 'NO', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(26, 'cfd PT', 'CFD - Portugal', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(27, 'cfd SE', 'CFD - Sweden', 'SE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(28, 'cfd CH', 'CFD - Switzerland', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(29, 'cfd ES', 'CFD - Spain', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(30, 'cfd other share', 'CFD - other share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(31, 'cfd AU', 'CFD - Australia', 'AU', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(32, 'cfd AT', 'CFD - Austria', 'AT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(33, 'cfd CN', 'CFD - China', 'CN', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(34, 'cfd PL', 'CFD - Poland', 'PL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(35, 'cfd SG', 'CFD - Singapore', 'SG', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(36, 'nyse', 'Ney York Stock Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(37, 'nasdaq', 'Nasdaq', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(38, 'otc bb & pinksheets', 'OTC BB & pinksheets', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(39, 'amex', 'American Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(40, 'other us', 'Other US markets', 'US', 1, current_date, current_date);

-- Add commodity names
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

-- Add specific parameters
/*INSERT INTO T_PARAMETER(parameter_id, name, value, description)
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
values(8, 'tax_dividend_nl', 0.15, 'dividend tax - NL');*/

-- Add specific margin types
/*INSERT INTO T_MARGIN_TYPE(margin_type)
values('safety');*/

-- Add specific margins
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

-- Add specific formulae
--TODO: add a column where you can say what the parameters are?
--TODO: add a table which contains the values for tax and commissions?
/*INSERT INTO T_FORMULA(formula_id, value, description)
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
values(5, '','commission us stocks');*/

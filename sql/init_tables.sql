/* markets */
INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('ams', 'Amsterdam', current_date, current_date);

INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('ebr', 'Brussels', current_date, current_date);

INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('dax', 'Germany', current_date, current_date);

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

/* products */
INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('account.rx', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('account.start', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('account.tx', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('bills.dexia', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('bills.internet', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('bills.mutuality', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('bills.police', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('bills.vik', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('car.buy', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('car.gas', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('car.insurance', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('car.maintenance', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('car.tax', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('extra.magazine', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('extra.other', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('extra.travel', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('extra.wallet', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('hobby.computer', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('hobby.martialarts', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('hobby.other', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('house.rent', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('house.maintenance', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('house.other', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.buystocks', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.changestocks', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.dividend', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.invest', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.refund', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('invest.sellstocks', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('refunds.mutuality', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('salary', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('tax.refund', current_date, current_date);

INSERT INTO T_PRODUCT(product, date_created, date_modified)
values('tax.tax', current_date, current_date);

/* margin types */
INSERT INTO T_MARGIN_TYPE(margin_type)
values('safety');

/* margins */
INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve after crossover', 1600000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safety margin passive income', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safe withdrawal rate', 0.03, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Bargain reserve', 100000, current_date, current_date);
COMMIT;

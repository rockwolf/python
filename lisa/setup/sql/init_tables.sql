BEGIN;
/* markets */
INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(1, '', '', '', 1, current_date, current_date);

/* stock names */
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('', 1, '', 1, current_date, current_date);

/* t_account */
INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(1, 'income', 'income', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(2, 'expenses', 'expenses', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(3, 'assets', 'assets', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(4, 'liabilities', 'liabilities', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(5, 'equity', 'equity', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(6, 'assets:prepaid_expenses', 'prepaid_expenses', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(7, 'liabilities:prepaid_income', 'prepaid_income', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(8, 'assets:accounts_receivable', 'accounts_receivable', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(9, 'liabilities:accounts_payable', 'accounts_payable', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(10, 'assets:current_assets', 'current_assets', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(account_id, name, description, active, date_created, date_modified)
values(11, 'assets:reimbursements', 'reimbursements', 1, current_date, current_date);

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
values(1, '{0}', 'Default: no formula needed, just use the value.');

/* t_rate */
INSERT INTO T_RATE(calculated, calculated_percent, on_shares, on_commission, on_ordersize, on_other, commission, tax, formula_id, automatic_flag, date_created, date_modified)
values(-1.0, -1.0/100, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1, 0, current_date, current_date);

/* t_parameter */
-- None

/* t_margin_types */
-- None

/* margins */
-- None

/* t_version */
INSERT INTO T_VERSION
values(1, '2.0', 'Lisa with trading options.', current_date, current_date);

COMMIT;

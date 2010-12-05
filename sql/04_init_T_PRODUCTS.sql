BEGIN;
INSERT INTO T_PRODUCTS(prod)
select distinct prod from T_FINANCE;
COMMIT;

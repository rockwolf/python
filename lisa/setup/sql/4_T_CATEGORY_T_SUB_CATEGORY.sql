/* Author: rockwolf
 * Date: 2012-08-03
 * Function: Database changes for renaming and refactoring
 * T_PRODUCT and T_OBJECT tot T_CATEGORY and T_SUB_CATEGORY.
 */
drop table T_PRODUCT;
drop table T_OBJECT;

CREATE TABLE T_CATEGORY
(
    cid serial not null,
    scid int not null default 1, --enter default value for scid for 'None' here.
    name varchar(30) not null,
    flg_income int not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_cid primary key(cid),
    constraint fk_foreign key(sub_category_id) references T_SUB_CATEGORY(scid)
);
CREATE TABLE T_SUB_CATEGORY
(
    scid serial not null,
    name varchar(20) not null,
    date_created timestamp not null default current_date,
    date_modified timestamp not null default current_date,
    constraint pk_scid primary key(scid)
);

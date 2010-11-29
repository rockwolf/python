CREATE TABLE T_PRODUCTS
(
    pid serial not null,
    prod varchar(30) not null,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_pid primary key(pid)
);

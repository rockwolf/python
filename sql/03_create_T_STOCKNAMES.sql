CREATE TABLE T_STOCKNAMES
(
    snid serial not null,
    name varchar(5) not null,
    mid int not null,
    description varchar(30),
    date_created timestamp,
    date_modified timestamp,
    constraint pk_snid primary key(snid),
    constraint fk_mid foreign key(mid) references T_MCODES(mid)
);

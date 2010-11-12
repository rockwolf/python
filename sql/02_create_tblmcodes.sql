CREATE TABLE mcodes
(
    mid serial not null,
    mcode varchar(3) not null,
    description varchar(30),
    date_created timestamp,
    date_modified timestamp,
    constraint pk_mid primary key(mid)
);

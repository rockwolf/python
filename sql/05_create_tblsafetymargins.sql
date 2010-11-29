CREATE TABLE T_SAFETYMARGINS
(
    smid serial not null,
    description varchar(100) not null,
    value decimal(18,4) not null default 0.0,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_smid primary key(smid)
);

CREATE TABLE T_TEAMS
(
    tid serial not null,
    name varchar(30) not null,
    division varchar(30),
    active int not null default 1,
    date_created timestamp,
    date_modified timestamp,
    constraint pk_tid primary key(tid)
);

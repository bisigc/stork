drop table if exists task;
create table task (
id integer primary key autoincrement,
title text not null,
description text,
duedate text,
creator_id integer not null,
assignee_id integer,
project_id integer,
finished integer not null,
created real not null,
modified real not null);

drop table if exists note;
create table note (
id integer primary key autoincrement,
note text,
creator_id integer not null,
task_id integer not null,
created real not null,
modified real not null);

drop table if exists project;
create table project (
id integer primary key autoincrement,
title text,
description text,
creator_id integer not null,
created real not null,
modified real not null);

drop table if exists user;
create table user (
id integer primary key autoincrement,
username text not null,
password text not null,
firstname text,
surname text,
email text not null,
mobile text,
created real not null,
modified real not null);


insert into user (username, password, email, created, modified) VALUES ('cbi', 'test', 'cbisig@gmail.com', date('now'), date('now'));


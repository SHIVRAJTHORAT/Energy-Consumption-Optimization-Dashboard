create table enery_usage(
id serial primary key,
timestamp timestamp,
location varchar(50),
appliance varchar(50),
consumption_kwh FLOAT,
temperature float,
weather varchar(20)
);
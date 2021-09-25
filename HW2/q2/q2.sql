drop table rdata;
CREATE TABLE rdata (
id SERIAL PRIMARY KEY,
a varchar(5) UNIQUE NOT NULL,
b varchar(5) UNIQUE NOT NULL,
Moment DATE default '2020-01-01',
x numeric(5,2) check (x>0)  
);
select * from rdata;
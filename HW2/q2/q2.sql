drop table rdata;
CREATE TABLE rdata (
id SERIAL PRIMARY KEY,
a TEXT UNIQUE NOT NULL CHECK (char_length(a) <=5),
b TEXT UNIQUE NOT NULL CHECK (char_length(b) <=5),
Moment DATE default '2020-01-01',
x INT check (x>0)  
);
-- Creating index on employees table (Allows duplicates)
create index id
on employees(name,salary);

-- Creating Unique index (Does not allow duplicates)
create unique index idx
on employees(name);

-- Deleting Indexes
drop index idx
on employees;           -- Approach 1

alter table employees
drop index id;          -- Approach 2

-- UNIQUE Query
create table users(
user_id INT Primary key,
user_name VARCHAR(20),
email VARCHAR(30),
unique(user_name,email));   -- Sets both the columns as unique and does not allow duplicate records

-- deleting unique fields from a table
alter table users
drop email;               
USE sample;
create table students(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20));
select * from students;

insert into students(name,age) values('k',10);
ALTER TABLE students
ADD age INT;

ALTER TABLE students
RENAME COLUMN class TO gpa;

ALTER TABLE students
modify column gpa decimal;

delete from students
where id=1;

use world;

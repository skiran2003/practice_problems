SELECT * FROM customers
WHERE customerName LIKE 'G%';

SELECT * FROM customers
WHERE customerName LIKE '%ltd';

SELECT * FROM customers
WHERE customerName LIKE '%auto%';

SELECT * FROM customers
WHERE customerName LIKE '___Stores,Co.';

USE sample;
select * from departments d join subjects s on d.deptno=s.deptno
where d.deptno not in(1,2);
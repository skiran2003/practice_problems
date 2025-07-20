SELECT * FROM customers
WHERE country = 'USA';

SELECT customerName,city FROM customers
WHERE country = 'France';

SELECT * FROM customers
WHERE creditLimit > 100000;

-- IN,AND 
SELECT * FROM customers
WHERE country in ('India','USA') and creditLimit > 80000;

-- IS NULL
SELECT * FROM orders
WHERE comments IS NULL;

-- Not equal to (<> or !=)
SELECT * FROM customers
WHERE country <> 'France' OR 'Germany';

SELECT * FROM customers
WHERE country != 'USA' AND creditLimit BETWEEN 60000 AND 100000;
USE havingclause_practice;

-- Find customers who have placed at least one order.

select c.name , c.customer_id from customers c
where exists( select * from orders o where c.customer_id = o.customer_id);

-- Find products that have never been ordered.

select p.name , p.product_id from products p
where not exists (select * from order_items o where o.product_id = p.product_id);

-- Write a query using EXISTS to find all employees who belong to departments that exist in the departments table.

select * from employees e
where exists(select * from departments d where d.department_id = e.department_id);

-- Find employees who work in a department that has more than 10 employees.

select e1.name , e1.employee_id from employees e1
where exists (select count(*) from employees e2 where e1.department_id = e2.department_id
group by e2.department_id having count(e2.department_id) > 10); 

-- Find customers who have ordered a product that belongs to category 'Electronics'.

select * from customers c
where exists (select * from orders o where o.customer_id = c.customer_id and exists
(select * from order_items oi where oi.order_id = o.order_id and exists 
(select * from products p where p.product_id=oi.product_id and p.category = 'Electronics')));
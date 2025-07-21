-- Find customers who have ordered both 'Electronics' and 'Books'.
select distinct c.name from customers c
join orders o on o.customer_id=c.customer_id
join order_items oi on o.order_id=oi.order_id
join products p on p.product_id=oi.product_id
where p.category = 'Electronics' or p.name = 'Book';

-- Get a list of employees and their departments. Also include employees who are not assigned to any department.

select e.name, e.department_id , d.name from employees e
left join departments d on d.department_id = e.department_id;

-- List customers who have ordered products in the 'Electronics' category.

select c.name, c.customer_id from customers c
join orders o on o.customer_id=c.customer_id
join order_items oi on oi.order_id=o.order_id
where exists (select * from products p where p.product_id = oi.product_id and p.category = 'Electronics');
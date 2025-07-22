-- Display employee names and a new column status based on their salary:

select name, salary,
case
when salary<30000 then "Low"
when salary>30000 and salary<70000 then "Medium"
else "High"
end as 'status' from employees;

-- Retrieve names of employees whose salary is greater than at least one employee working in the 'Sales' department.

select name from employees
where salary>any(select e.salary from employees e 
join departments d on d.department_id=e.department_id 
where d.name='Sales');

-- Find products that are priced higher than all products in the "Electronics" category.

select name,price from products
where price > all(select price from products where category = 'Electronics');


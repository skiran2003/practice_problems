-- Write a query to rank employees by salary within their department using RANK() or DENSE_RANK().
select name, salary,
dense_rank() over(order by salary desc) as salary_rank from employees; -- Gives same rank to similar salaries 

select name, salary,
rank() over(order by salary desc) as 'Rank' from employees; -- Gives different rank to similar salaries

-- Write a query to calculate the average salary, maximum, and minimum salary from the employees table.
select max(salary) as max_salary, min(salary) as min_salary, avg(salary) as average_salary
from employees group by department_id;


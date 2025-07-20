use havingclause_practice;

-- Find departments that have more than 4 employees. 

select department_id, count(*) as 'Employee Count' from employees
group by department_id
having count(department_id) > 4;

-- Find job titles where the average salary is less than 50,000.

select job_title, avg(salary) as 'Average salary' from employees
group by job_title
having avg(salary) < 50000;

-- List all departments where the total salary is above 1,00,000 and the number of employees is more than 3.

select d.name, count(e.employee_id) , sum(e.salary) from employees e
join departments d on d.department_id = e.department_id
group by d.name
having count(e.employee_id) > 3 and sum(e.salary) > 100000;

-- Show job titles that have at least one employee earning more than 80,000.

select job_title , max(salary) from employees
group by job_title
having max(salary) > 80000;

-- Get the department names where the average salary (as avg_sal) exceeds 60,000.

select d.name, avg(e.salary) as avg_sal from employees e
join departments d on d.department_id = e.department_id
group by d.name
having avg(e.salary) > 60000;
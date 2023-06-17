select employee_id, name, reports_count, average_age
from Employees t1
join (select reports_to, ROUND(AVG(age)) as average_age, COUNT(age) as reports_count
from Employees
where reports_to is not null
group by 1) t2
on t1.employee_id = t2.reports_to
order by t1.employee_id;
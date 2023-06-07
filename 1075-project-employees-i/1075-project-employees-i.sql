select project_id, ROUND(SUM(experience_years)/COUNT(name),2) average_years
from Project
left join Employee
using(employee_id)
group by project_id;
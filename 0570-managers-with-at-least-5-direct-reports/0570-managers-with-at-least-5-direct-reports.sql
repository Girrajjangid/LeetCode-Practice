select name
from employee as t1
left join (select managerId as id, count(managerId) as counts
from employee
group by managerId) as t2
using(id)
where counts >= 5;
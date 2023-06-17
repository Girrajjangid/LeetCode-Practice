select employee_id, department_id
from (select *, COUNT(*) OVER(PARTITION BY employee_id) as cnt
from Employee) t1
where (cnt=1) or (cnt<>1 and primary_flag='Y');
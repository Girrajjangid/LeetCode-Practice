select person_name 
from (select *, sum(weight) OVER(order by turn) cumsum
from Queue) t1
where t1.cumsum <= 1000
ORDER BY turn DESC
LIMIT 1;
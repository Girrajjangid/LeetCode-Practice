select student_id, student_name, subject_name, IF(attended_exams is NULL,0,attended_exams) as attended_exams
from (select * from students cross join subjects) as t1
left join
(select student_id, subject_name, count(*) as attended_exams
from examinations
group by student_id, subject_name) as t2
using(student_id, subject_name)
order by student_id, subject_name;
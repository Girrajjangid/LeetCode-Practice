select machine_id, round(sum(end-start)/count(machine_id), 3) as processing_time
from (select machine_id, process_id, timestamp as start
from activity
where activity_type = 'start') as t1
join (select machine_id, process_id, timestamp as end
from activity
where activity_type = 'end') as t2
using(machine_id, process_id)
group by machine_id;
select product_id,  ROUND(SUM(price_unit)/SUM(units), 2) as average_price
from (select *, price*units as price_unit
from prices
left join unitssold
using(product_id)
where purchase_date BETWEEN start_date and end_date) as t1
group by product_id;
SELECT ROUND(AVG(IF(t1.order_date=t1.customer_pref_delivery_date,1,0))*100,2) as immediate_percentage
FROM (select * , ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date ASC) as RowNum
FROM Delivery) as t1
WHERE RowNum=1;
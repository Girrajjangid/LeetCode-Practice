# Write your MySQL query statement below

SELECT product_id, year AS first_year, quantity, price
FROM (SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY year ASC) AS row_num FROM Sales) t1
WHERE row_num = 1;

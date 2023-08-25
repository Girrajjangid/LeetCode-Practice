# Write your MySQL query statement below

SELECT t2.name AS Department, t1.name AS Employee, t1.salary AS Salary
FROM (SELECT *, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as cnt from Employee) t1
JOIN Department t2
ON t1.departmentID = t2.id
WHERE cnt <= 3
ORDER BY t2.name, t1.salary DESC;
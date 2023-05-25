# Write your MySQL query statement below



SELECT CASE WHEN Employees.id = EmployeeUNI.id THEN EmployeeUNI.unique_id ELSE Null END as unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
on Employees.id = EmployeeUNI.id;
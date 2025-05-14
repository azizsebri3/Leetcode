# Write your MySQL query statement below
SELECT EU.unique_id , E.name
FROM EmployeeUNI EU
RIGHT JOIN Employees E ON E.id = EU.id

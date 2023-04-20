# Write your MySQL query statement below

# 1st solution
SELECT E.name as "name", B.bonus as "bonus" FROM Employee E left join Bonus B
ON E.empId = B.empId 
WHERE bonus IS NULL OR bonus < 1000
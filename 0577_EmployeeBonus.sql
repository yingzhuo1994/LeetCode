# Write your MySQL query statement below

# 1st solution
SELECT T.name, T.bonus from (
SELECT E.name as "name", B.bonus as "bonus" FROM Employee E left join Bonus B
ON E.empId = B.empId
) T
WHERE T.bonus IS NULL OR T.bonus < 1000 
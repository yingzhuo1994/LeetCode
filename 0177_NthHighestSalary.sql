Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

# 1st solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
        SELECT
            (SELECT DISTINCT
                    salary
                FROM
                    Employee
                ORDER BY salary DESC
                LIMIT 1 OFFSET M)
  );
END
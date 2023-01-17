Create table If Not Exists Weather (id int, recordDate date, temperature int)
Truncate table Weather
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')

# Write your MySQL query statement below
SELECT
    w1.id AS 'Id'
FROM
    weather w1
        JOIN
    weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
        AND w1.Temperature > w2.Temperature
;
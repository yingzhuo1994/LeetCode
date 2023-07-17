# Write your MySQL query statement below
select * from Cinema t
where (t.id % 2) = 1 and t.description != "boring"
order by rating desc
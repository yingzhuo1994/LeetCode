# Write your MySQL query statement below
# 1st solution
with t as (select case
when id % 2 = 1 then id + 1
else  id - 1 
end as newid, student from Seat)

select ROW_NUMBER() OVER() as id, student from t
order by newid
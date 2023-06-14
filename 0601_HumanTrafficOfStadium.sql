# Write your MySQL query statement below

# 1st solution
select S.id, S.visit_date, S.people from Stadium S
where S.id in (select id from Stadium where people >= 100) and 
(
((S.id - 1) in (select id from Stadium where people >= 100) and (S.id - 2) in (select id from Stadium where people >= 100)) 
or ((S.id + 1) in (select id from Stadium where people >= 100) and (S.id + 2) in (select id from Stadium where people >= 100))
or ((S.id + 1) in (select id from Stadium where people >= 100) and (S.id - 1) in (select id from Stadium where people >= 100))
)

# 2nd solution
with t as ( select t1.id , t1.visit_date , t1.people , 
            id - row_number() OVER(ORDER BY id) as grp
       from stadium t1
       where people >= 100 
          )
select t.id, t.visit_date ,t.people
from t 
where grp in ( select grp from t group by grp having count(*) >=3 )
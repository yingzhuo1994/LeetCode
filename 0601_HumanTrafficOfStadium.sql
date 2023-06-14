# Write your MySQL query statement below

# 1st solution
select S.id, S.visit_date, S.people from Stadium S
where S.id in (select id from Stadium where people >= 100) and 
(
((S.id - 1) in (select id from Stadium where people >= 100) and (S.id - 2) in (select id from Stadium where people >= 100)) 
or ((S.id + 1) in (select id from Stadium where people >= 100) and (S.id + 2) in (select id from Stadium where people >= 100))
or ((S.id + 1) in (select id from Stadium where people >= 100) and (S.id - 1) in (select id from Stadium where people >= 100))
)

# Write your MySQL query statement below
# 1st solution
with t as
(select requester_id as "id", accepter_id as "other" from RequestAccepted
union
select accepter_id as "id", requester_id as "other" from RequestAccepted)

select id, count(*) as "num" from t
group by id
order by count(*) desc
limit 1

# 2nd solution
# Write your MySQL query statement below
select id, count(*) num from 
(
      (select requester_id id from RequestAccepted) 
      union all 
      (select accepter_id id from RequestAccepted)
) tb 
group by id order by num desc limit 1
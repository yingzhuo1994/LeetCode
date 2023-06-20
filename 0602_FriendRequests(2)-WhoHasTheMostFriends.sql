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
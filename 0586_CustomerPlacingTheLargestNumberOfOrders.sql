# Write your MySQL query statement below

# 1st solution
select t1.customer_number from
(select customer_number, count(order_number) as "order_count" from Orders group by customer_number) t1
order by t1.order_count desc
limit 1
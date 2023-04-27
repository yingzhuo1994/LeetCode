# Write your MySQL query statement below

# 1st solution
select customer_number from orders
group by customer_number
order by count(*) desc limit 1;
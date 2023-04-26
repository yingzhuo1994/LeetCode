# Write your MySQL query statement below
select round(sum(t.tiv_2016), 2) as "tiv_2016" from
(select distinct(t1.pid), t1.tiv_2016 from
(select * from Insurance group by lat, lon having count(*) = 1) t1, Insurance t2
where t1.pid != t2.pid and t1.tiv_2015 = t2.tiv_2015) t
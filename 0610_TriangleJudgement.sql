# Write your MySQL query statement below
select x, y, z, if((x + y > z and ABS(x - y) < z), "Yes", "No") as "triangle"
from Triangle
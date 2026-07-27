# Write your MySQL query statement below
select *
from Cinema
where description not in ('boring') and id%2=1
order by rating desc;

# Write your MySQL query statement below
select * from (select e.score, dense_rank() over(order by score desc) as 'rank' from Scores e)t;
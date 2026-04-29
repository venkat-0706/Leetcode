# Write your MySQL query statement below
select user_id, email
from Users 
where email REGEXP '^[a-z0-9_]+@[^@0-9]+\\.com$' 
group by user_id
order by user_id asc;
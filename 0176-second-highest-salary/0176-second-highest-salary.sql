# Write your MySQL query statement below
select max(distinct salary) as 'SecondHighestSalary'
from(
    select *, dense_rank() over(order by salary desc) as rnk from Employee
) as t
where rnk = 2;
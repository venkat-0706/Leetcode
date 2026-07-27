select max(distinct salary) as 'SecondHighestSalary'
from (select *, dense_rank() over(order by salary desc) as rnk from Employee) as x 
where rnk = 2;
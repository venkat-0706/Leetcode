select a.name 
from Employee a
join Employee b
on a.id  = b.managerId
group by b.managerId
having count(*) >= 5;
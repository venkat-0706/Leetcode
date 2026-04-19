update Salary 
set sex = case 
when sex ='m' then 'f'
when sex = 'f' then 'm'
end;
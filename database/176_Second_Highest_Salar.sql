-- use union to return null when there are no query return
select DISTINCT(`Salary`) as SecondHighestSalary FROM `Employee` UNION SELECT NULL ORDER BY SecondHighestSalary DESC LIMIT 1,1;

-- This works in mysql, but fail in leetcode with internal error
select max(Salary) as SecondHighestSalary
from (select distinct(Salary) from Employee order by Salary desc limit 1,1) as tmp;


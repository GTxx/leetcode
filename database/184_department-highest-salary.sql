select d.Name as Department, e.Name as Employee, e.Salary as Salary
from `Employee` e join Department d on e.DepartmentId= d.Id
where (e.Salary, e.DepartmentId) in
(select max(Salary), DepartmentId from `Employee` GROUP BY DepartmentId);
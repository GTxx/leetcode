select name as Customers
from Customers
where Id not in (select DISTINCT CustomerId from Orders);
# Write your MySQL query statement below

select Name as Customers
from Customers
where Customers.Id Not In
(Select CustomerId from Orders)
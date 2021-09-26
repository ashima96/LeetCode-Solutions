# Write your MySQL query statement below
select emp.Name as Employee from Employee as emp, Employee as mgr where emp.ManagerId <> "null" and emp.Salary > mgr.Salary and emp.ManagerId = mgr.Id;

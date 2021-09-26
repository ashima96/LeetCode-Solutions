# Write your MySQL query statement below
select Email from Person Group By Email Having Count(*) >1;
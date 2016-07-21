select Email from
(select Email, count(*) as num from Person group by Email) p
where num > 1;
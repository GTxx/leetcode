select class from 
(select count(distinct student) as cnt, class from courses group by class) as tmp 
where cnt >= 5;

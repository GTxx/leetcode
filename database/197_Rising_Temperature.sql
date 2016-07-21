-- This is my solution, also tried DATE_ADD, but leetcode returns internal error
select w2.Id from Weather w1
join Weather w2 on ADDDATE(w1.Date, INTERVAL 1 day) = w2.Date
where w2.Temperature > w1.Temperature;

-- Below solutions are from leetcode discuss
select w2.Id from Weather w1
join Weather w2 on w1.Date + INTERVAL 1 day = w2.Date
where w2.Temperature > w1.Temperature;

SELECT w1.Id FROM Weather w1, Weather w2
WHERE subdate(w1.Date, 1)=w2.Date AND w1.Temperature>w2.Temperature

Select W2.Id
from Weather W1, Weather W2
where W2.Temperature > W1.Temperature
and DATEDIFF(W2.Date,W1.Date)=1;

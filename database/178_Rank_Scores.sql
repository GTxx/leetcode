-- subquery accour in every row.
select Score,
(select count(*) from (select distinct score s from Scores) tmp where tmp.s >= score) as Rank
from Scores order by score desc;
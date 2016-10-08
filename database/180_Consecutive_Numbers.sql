select distinct(l1.Num) as ConsecutiveNums from `Logs` l1
join `Logs` l2 on l1.`Id`+1 = l2.id
join `Logs` l3 on l1.`Id`+2 = l3.id
where l1.`Num` = l2.`Num` and l1.`Num` = l3.Num;
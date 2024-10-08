# Write your MySQL query statement below
select visits.customer_id, count(visits.visit_id) as count_no_trans
from visits
left join Transactions
on visits.visit_id = Transactions.visit_id
where transactions.transaction_id is NULL
group by visits.customer_id;
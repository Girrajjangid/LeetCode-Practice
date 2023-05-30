SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM Visits
NATURAL LEFT JOIN Transactions
WHERE transaction_id is NULL
GROUP BY customer_id
ORDER BY COUNT(customer_id) DESC;
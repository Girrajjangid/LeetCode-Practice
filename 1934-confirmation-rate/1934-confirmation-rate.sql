select user_id, ROUND(AVG(IF(action = 'confirmed', 1, 0)), 2) as confirmation_rate
FROM Signups a
LEFT JOIN Confirmations b 
USING(user_id)
GROUP BY user_id;
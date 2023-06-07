SELECT contest_id, ROUND((COUNT(user_id)/(SELECT COUNT(DISTINCT(user_id)) FROM users))*100, 2) as percentage
FROM users
JOIN register
USING(user_id)
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
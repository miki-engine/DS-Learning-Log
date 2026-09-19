SELECT
    membership,
    COUNT(*) AS member_count,
    AVG(age) AS average_age
FROM users
GROUP BY membership;
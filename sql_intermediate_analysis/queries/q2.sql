SELECT
    u.user_name,
    u.membership,
    SUM(o.quantity * p.price) AS total_spent
FROM orders AS o
INNER JOIN products AS p
    ON o.product_id = p.product_id
INNER JOIN users AS u
    ON o.user_id = u.user_id
GROUP BY
    u.user_id,
    u.user_name,
    u.membership
ORDER BY total_spent DESC;
WITH
    purchased_electronics AS (
        SELECT
            o.user_id,
            COUNT(*) AS electronics_purchase_count
        FROM orders AS o
        WHERE o.product_id IN (
            SELECT p.product_id
            FROM products AS p
            WHERE p.category = 'Electronics'
        )
        GROUP BY o.user_id
    )

SELECT 
    u.user_name,
    e.electronics_purchase_count
FROM users AS u
INNER JOIN purchased_electronics AS e
    ON u.user_id = e.user_id
WHERE
    e.electronics_purchase_count >= 2;
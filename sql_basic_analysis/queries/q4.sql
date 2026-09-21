SELECT
    order_id,
    amount,
    CASE
        WHEN amount >= 30000 THEN 'High'
        WHEN amount >= 10000 THEN 'Medium'
        ELSE 'Low'
    END AS price_class
FROM orders;
SELECT
    orders.order_id,
    orders.order_date,
    products.product_name,
    products.price,
    orders.quantity,
    (products.price * orders.quantity) AS sales_amount
FROM orders
INNER JOIN products
    ON orders.product_id = products.product_id;
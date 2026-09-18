SELECT *
FROM orders
WHERE category = 'Electronics'
  AND amount >= 30000
ORDER BY amount DESC;
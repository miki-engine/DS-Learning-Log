SELECT
    revenue_month,
    category,
    revenue,
    RANK() OVER (PARTITION BY revenue_month ORDER BY revenue DESC) AS sales_rank
FROM category_monthly_revenue
ORDER BY revenue_month ASC, sales_rank ASC;
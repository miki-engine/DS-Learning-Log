SELECT
    revenue_month,
    category,
    revenue,
    SUM(revenue) OVER (
        PARTITION BY category
        ORDER BY revenue_month ASC
    ) AS cumulative_revenue
FROM category_monthly_revenue
ORDER BY category ASC, revenue_month ASC;
WITH category_revenue AS (
    SELECT
        category,
        revenue_month,
        revenue,
        RANK() OVER (
            PARTITION BY category
            ORDER BY revenue DESC
        ) AS category_rank
    FROM category_monthly_revenue
)

SELECT
    category,
    revenue_month,
    revenue
FROM category_revenue
WHERE category_rank = 1
ORDER BY category ASC;
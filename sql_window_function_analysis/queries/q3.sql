WITH revenue_comparison AS (
    SELECT
        revenue_month,
        category,
        revenue,
        LAG(revenue) OVER (
            PARTITION BY category
            ORDER BY revenue_month ASC
        ) AS previous_month_revenue
    FROM category_monthly_revenue
)

SELECT
    revenue_month,
    category,
    revenue,
    previous_month_revenue,
    revenue - previous_month_revenue AS revenue_diff
FROM revenue_comparison
ORDER BY category ASC, revenue_month ASC;
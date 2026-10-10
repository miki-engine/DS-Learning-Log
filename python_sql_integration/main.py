import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "ecommerce.db"

csv_paths = {
    "orders": DATA_DIR / "orders.csv",
    "products": DATA_DIR / "products.csv",
    "users": DATA_DIR / "users.csv",
}

dfs = {
    table_name: pd.read_csv(csv_path)
    for table_name, csv_path in csv_paths.items()
}

conn = sqlite3.connect(DB_PATH)

try:
    for table_name, df in dfs.items():
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False,
        )

    category = "Electronics"

    sales_query = """
    SELECT
        p.product_name,
        SUM(o.quantity) AS total_quantity,
        SUM(p.price * o.quantity) AS total_revenue
    FROM products AS p
    INNER JOIN orders AS o
        ON p.product_id = o.product_id
    WHERE p.category = ?
    GROUP BY p.product_name
    ORDER BY total_revenue DESC;
    """

    result_df = pd.read_sql_query(
        sales_query,
        conn,
        params=(category,),
    )

    print(result_df)

finally:
    conn.close()
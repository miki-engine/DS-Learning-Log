import sqlite3
from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent / "data"
ORDERS_PATH = DATA_DIR / "orders.csv"
PRODUCTS_PATH = DATA_DIR / "products.csv"
USERS_PATH = DATA_DIR / "users.csv"
DB_PATH = Path(__file__).resolve().parent / "ecommerce.db"

df_orders = pd.read_csv(ORDERS_PATH)
df_products = pd.read_csv(PRODUCTS_PATH)
df_users = pd.read_csv(USERS_PATH)

dfs = {
    "orders": df_orders,
    "products": df_products,
    "users": df_users,
}

for name, df in dfs.items():
    print(f"---{name}---")
    print(f"Size (shape): {df.shape}")
    print(df.head())
    print("-" * 40)

conn = sqlite3.connect(DB_PATH)

try:

    df_orders.to_sql("orders", conn, if_exists="replace", index=False)
    df_products.to_sql("products", conn, if_exists="replace", index=False)
    df_users.to_sql("users", conn, if_exists="replace", index=False)


finally:

    conn.close()
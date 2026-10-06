import sqlite3
from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent / "data"
ORDERS_PATH = DATA_DIR / "orders.csv"
PRODUCTS_PATH = DATA_DIR / "products.csv"
USERS_PATH = DATA_DIR / "users.csv"

df_orders = pd.read_csv(ORDERS_PATH)
df_products = pd.read_csv(PRODUCTS_PATH)
df_users = pd.read_csv(USERS_PATH)
from pathlib import Path

import pandas as pd


base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data" / "sales_logs.csv"

sales_logs = pd.read_csv(csv_path)

result = pd.pivot_table(
    sales_logs,
    index="rank",
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0
)

print(result)
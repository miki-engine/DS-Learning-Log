# 1. Customer master data（For initial registration）
customer_master = [
    {"customer_id": "C001", "name": "Alice"},
    {"customer_id": "C002", "name": "Bob"},
    {"customer_id": "C003", "name": "Charlie"}
]

# 2. Purchase action log
purchase_actions = [
    {"customer_id": "C001", "amount": 5000},
    {"customer_id": "C002", "amount": 2000},
    {"customer_id": "C001", "amount": 8000},
    {"customer_id": "C003", "amount": 15000},
    {"customer_id": "C001", "amount": 2000},
]

class Customer:
    def __init__(self, customer_id, name):
        pass

    def add_purchas(self, amount):
        pass

    def get_rank(self):
        pass


if __name__ == "main":
    customers = {}
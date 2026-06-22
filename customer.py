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
    """
    Represents a customer and tracks their purchase history.
    
    Attributes:
        customer_id (str): The unique identifier for the customer.
        name (str): The customer's name.
        total_amount (int): The cumulative purchase amount.
    """


    def __init__(self, customer_id, name):
        """
        Save customer_id and name. Then initialize total_amount to 0.

        Args:
            customer_id (str): The unique identifier for the customer.
            name (str): The customer's name.
        """
        self.customer_id = customer_id
        self.name = name
        self.total_amount = 0



    def add_purchase(self, amount):
        pass


    def get_rank(self):
        pass


if __name__ == "__main__":
    customers = {}
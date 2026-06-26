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
        """
        Add amount to total_amount.

        Args:
            amount (int): The purchase amount.
        """
        self.total_amount += amount


    def get_rank(self):
        """
        Rank determined based on total_amount.

        Returns:
            rank (str): If the total_amount is 10000 or more, return VIP.
            Otherwise return Standard.
        """
        if self.total_amount >= 10000:
            rank = "VIP"
        else:
            rank = "Standard"

        return rank


if __name__ == "__main__":
    customers = {}
    for customer in customer_master:
        cid = customer["customer_id"]
        name = customer["name"]
        new_customer = Customer(cid, name)
        customers[cid] = new_customer

    for action in purchase_actions:
        cid = action["customer_id"]
        amount = action["amount"]
        target_customer = customers[cid]
        target_customer.add_purchase(amount)

    print("ID   |   Name   | Total amount | Rank")

    for cid, target_customer in customers.items():
        customer_id = target_customer.customer_id
        name = target_customer.name
        total_amount = target_customer.total_amount
        rank = target_customer.get_rank()

        print(f"{cid} | {name:8} | {total_amount:12} | {rank}")


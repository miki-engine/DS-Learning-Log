# 1. Campaign master data (planning budget data)
# cost: advertising cost
campaign_master = [
    {"campaign_id": "CMP_01", "name": "Summer_Sale", "cost": 50000},
    {"campaign_id": "CMP_02", "name": "Welcome_Coupon", "cost": 20000},
    {"campaign_id": "CMP_03", "name": "Email_Newsletter", "cost": 5000}
]

# 2. Purchase log via campain (dummy data）
# Include invalid data (amount is 0 or less)
conversion_logs = [
    {"campaign_id": "CMP_01", "amount": 15000},
    {"campaign_id": "CMP_02", "amount": 8000},
    {"campaign_id": "CMP_01", "amount": 25000},
    {"campaign_id": "CMP_01", "amount": -3000}, # invalid data
    {"campaign_id": "CMP_03", "amount": 3000},
    {"campaign_id": "CMP_02", "amount": 12000},
    {"campaign_id": "CMP_01", "amount": 40000},
    {"campaign_id": "CMP_03", "amount": 4500},
    {"campaign_id": "CMP_02", "amount": 5000},
]


class Campaign:
    """
    
    """


    def __init__(self, campaign_id, name, cost):
        """
        """
        pass


    def add_conversion(self, amount):
        """
        """
        pass


    def calculate_cpa(self):
        """
        """
        pass

    def calculate_roi(self):
        """
        """
        pass


if __name__ == "__main__":
    campaigns = {}
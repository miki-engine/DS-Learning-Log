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
    Represents a campaign and tracks its history.

    Attributes:
        campaign_id (str): The unique identifier for the campaign.
        name (str): The campaign's name.
        cost (int): The cost of the campaign.
        conversions (int): The number of conversions acquired through the campaign.
        revenue (int) : The total sales generated through the campaign.
    """


    def __init__(self, campaign_id, name, cost):
        """
        Save campaign_id, name, and cost. Then initialize conversions and revenue to 0.

        Args:
            campaign_id (str): The unique identifier for the campaign.
            name (str): The campaign's name.
            cost (int): The cost of the campaign.
        """
        self.campaign_id = campaign_id
        self.name = name
        self.cost = cost
        self.conversions = 0
        self.revenue = 0


    def add_conversion(self, amount):
        """
        Add amount to revenue and 1 to conversions.

        Args:
            amount (int): The sales generated through the campaign.
        """
        if amount > 0:
            self.conversions += 1
            self.revenue += amount


    def calculate_cpa(self):
        """
        Calculate the cost per acquisition (CPA) to acquire one purchase.

        Returns:
            float: The cost per acquisition (CPA), or 0 if there are no conversions.
        """
        if self.conversions <= 0:
            cpa = 0
        else:
            cpa = self.cost / self.conversions
        
        return cpa
        


    def calculate_roi(self):
        """
        Calculate the percentage of profit (ROI) generated relative to the costs incurred.

        Returns:
            float: The percentage of profit (ROI).
        """
        if self.cost <= 0:
            roi = 0
        else:
            roi = (self.revenue - self.cost) / self.cost * 100
        return roi


if __name__ == "__main__":
    campaigns = {}
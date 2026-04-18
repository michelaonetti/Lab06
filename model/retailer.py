class Retailer:
    def __init__(self, Retailer_code, Retailer_name, Type, Country):
        self.retailer_code = Retailer_code
        self.retailer_name = Retailer_name
        self.type = Type
        self.country = Country

    def __hash__(self):
        return hash(self.retailer_code)

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __str__(self):
        return f"{self.retailer_name}"
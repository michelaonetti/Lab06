class Sale:
    def __init__(self, Retailer_code, Product_number,Order_method_code, Date, Quantity, Unit_price, Unit_sale_price, Ricavo):
        self.date = Date
        self.quantity = Quantity
        self.unit_price = Unit_price
        self.order_method_code = Order_method_code
        self.unit_sale_price = Unit_sale_price
        self.retailer_code = Retailer_code
        self.product_number = Product_number
        self.ricavo = Ricavo
        self.retailer = None # Verrà popolato dall'Identity Map nel Model

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo:.2f}; Retailer: {self.retailer_code}; Product: {self.product_number}"
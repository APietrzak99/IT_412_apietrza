class InventoryItem():
    """A virtual representation of an inventory system"""

    def __init__(self, whofor):
        """Constructor for InventoryItem class"""
        self.whofor = whofor
        self.quantity_total_purchased = []
        self.productID = 1000
        self.product_name = "bookmarks"
        self.quantity = 46  

    def buy_item(self, purchased_quantity):
        """removes stock from the current quantity, simulates buying a product"""
        if purchased_quantity == "":
            self.quantity -= 1
            self.quantity_total_purchased.append(1)
        elif int(purchased_quantity):
            self.quantity -= purchased_quantity
            self.quantity_total_purchased.append(purchased_quantity)
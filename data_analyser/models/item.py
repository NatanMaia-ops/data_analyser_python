class Item:
    def __init__(self, item_id: int, quantity: int, price: float):
        self.item_id = item_id
        self.quantity = quantity
        self.price = price

    def total(self)->float:
        return self.quantity * self.price
    


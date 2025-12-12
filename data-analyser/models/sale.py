class Sale:
    def __init__(self, sale_id: str, items: list, salesman: str):
        self.sale_id = sale_id
        self.items = items
        self.salesman = salesman


    def total(self)->float:
        return sum(item.total() for item in self.items)
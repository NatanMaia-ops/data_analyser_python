from data_analyser.models.item import Item
from data_analyser.models.sale import Sale

def parse(line: str)-> Sale:
    _, sale_id, raw_items, salesman = line.split("ç")
    raw_items = raw_items.strip("[]").split(",")

    items = []
    for raw in raw_items:
        item_id, qty, price = raw.split("-")
        items.append(Item(int(item_id), int(qty), float(price)))

    return Sale(sale_id, items, salesman)
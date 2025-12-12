from data_analyser.parsers import seller_parser, custumer_parser, sale_parser

def read_file(path):
    sellers, custumers, sales = [], [], []

    with open(path, encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if line.startswith("001"):
                sellers.append(seller_parser.parse(line))
            elif line.startswith("002"):
                custumers.append(custumer_parser.parse)

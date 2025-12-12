from data_analyser.models.custumer import Custumer

def parse(line: str)-> Custumer:
    _, cnpj, name, business_area = line.split("ç")
    return Custumer(cnpj, name, business_area)

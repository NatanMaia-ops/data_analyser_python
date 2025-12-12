from data_analyser.models.seller import Seller

def parse(line: str)-> Seller:
   _, cpf, name, salary = line.split("ç")
   return Seller(cpf, name, float(salary))


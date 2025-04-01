class Retailer:
    def __init__(self, retailerCode, nome):
        self.retailerCode = retailerCode
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
from database.DAO import DAO

class Model:
    def __init__(self):
        self.dao = DAO()

    def getAnni(self):
        return self.dao.getAnni()

    def getProdotti(self):
        return self.dao.getProdotti()

    def getBrand(self):
        return self.dao.getBrand()
    def getRetailers(self):
        return self.dao.getRetailers()

    def getVenditeNoFiltri(self, anno, brand, retailer):
        return self.dao.getVenditeNoFiltri(anno, brand, retailer)

    def getVendite(self, anno, brand, retailer):
        return self.dao.getVendite(anno, brand, retailer)

    def AnalizzaVendite(self, anno, brand, retailer):
        return self.dao.AnalizzaVendite(anno, brand, retailer)
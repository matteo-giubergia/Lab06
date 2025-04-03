from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.product import Product
from model.vendita import Vendita

class DAO():
    def __init__(self):
        pass

    def getAnni(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT year(Date) 
                    FROM go_daily_sales"""
        cursor.execute(query)
        anni = []
        for anno in cursor.fetchall():
            if anno["year(Date)"] not in anni:
                anni.append(anno["year(Date)"])
        cursor.close()
        cnx.close()
        return anni

    def getVenditeNoFiltri(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        # query = """select s.`Date`, s.Unit_sale_price, s.Quantity, s.Product_number, s.Retailer_code
        #             from go_daily_sales s, go_products p
        #             where year(s.`Date`)=%s and p.Product_brand=%s and s.Retailer_code=%s"""
        query="""select s.`Date`, (s.Unit_sale_price*s.Quantity) as guadagno, s.Product_number, s.Retailer_code 
                     from go_daily_sales s
                     JOIN go_products p ON s.Product_number = p.Product_number
                     where s.Retailer_code = coalesce(%s, s.Retailer_code) and p.Product_brand = coalesce(%s, p.Product_brand)
                            and year(s.`Date`) = coalesce(%s, year(s.`Date`))  
                     order by guadagno desc
                     limit 5""" # o prende i valori in input o prende il primo a caso(?)
        cursor.execute(query, (anno, brand, retailer))
        vendite = []
        for r in cursor.fetchall():
            # guadagno = float(r["Unit_sale_price"])*float(r["Quantity"])
            vendite.append(Vendita(r["Date"], r["guadagno"],r["Product_number"] , r["Retailer_code"]))

        cursor.close()
        cnx.close()
        return vendite
    def getVendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query="""select s.`Date`, (s.Unit_sale_price*s.Quantity) as guadagno, s.Product_number, s.Retailer_code 
                     from go_daily_sales s, go_products p
                     where year(s.`Date`)=%s and p.Product_brand=%s and s.Retailer_code=%s and p.Product_number=s.Product_number
                     order by guadagno desc
                     limit 5"""
        cursor.execute(query, (anno, brand, retailer))
        vendite = []
        for r in cursor.fetchall():
            # guadagno = float(r["Unit_sale_price"])*float(r["Quantity"])
            vendite.append(Vendita(r["Date"], r["guadagno"],r["Product_number"] , r["Retailer_code"]))

        cursor.close()
        cnx.close()
        return vendite

    def AnalizzaVendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query="""select count(s.Product_number) as quantitaTot, count(distinct(s.Retailer_code)) as numretailers, count(distinct(s.Product_number)) as numProdDistinti,
                     sum(s.Unit_sale_price*s.Quantity) as guadagno
                     from go_daily_sales s, go_products p
                     where year(s.`Date`)=%s and p.Product_brand=%s and s.Retailer_code=%s and p.Product_number=s.Product_number
                     """
        cursor.execute(query, (anno, brand, retailer))
        vendite =  cursor.fetchall()

        cursor.close()
        cnx.close()
        return vendite

    def getProdotti(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select Product_number, Product from go_products"""
        cursor.execute(query)
        prodotti = [] #creo classe vendite con qualche attributo e le ordino con il metodo sort
        for p in cursor.fetchall():
            prodotti.append(Product(p["Product_number"], p["Product"]))
        cursor.close()
        cnx.close()
        return prodotti

    def getBrand(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select Product_brand from go_products"""
        cursor.execute(query)
        brands = []
        for b in cursor.fetchall():
            if b["Product_brand"] not in brands:
                brands.append(b["Product_brand"])
        cursor.close()
        cnx.close()
        return brands

    def getRetailers(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select Retailer_code, Retailer_name from go_retailers
                    order by Retailer_name asc"""
        cursor.execute(query)
        retailers = []
        for r in cursor.fetchall():
            if r not in retailers:
              retailers.append(Retailer(r["Retailer_code"],r["Retailer_name"]))
        cursor.close()
        cnx.close()
        return retailers




if __name__ == "__main__":
    dao = DAO()
    #print(dao.getVendite())

import datetime
import operator
from dataclasses import dataclass


@dataclass
class Vendita:
    data: str
    guadagno: float
    product_number: int
    retailer_code: int

    # ordinali in qualche modo

    def __str__(self):
        return f"Data: {self.data}; Ricavo: {self.guadagno}, Codice retailer: {self.retailer_code}, Numero prodotto: {self.product_number}"

                # guadagno viene restituito in modo un po' strano, potrebbe essere inizio di un errore

    # def ordinatePerGuadagno(self):
    #     lista.sorted(key=operator.attrgetter('guadagno'), reverse=True) #key = lambda v: v.guadagno, reverse=True

import operator

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def selezionaFiltri(self):
        brand = self._view.ddBrand.value
        anno = self._view.ddAnno.value
        retailer = self._view.ddRetailer.value
        if anno is None:
            self._view.create_alert("seleziona anno")
            return
        if brand is None:
            self._view.create_alert("seleziona brand")
            return
        if retailer is None:
            self._view.create_alert("seleziona retailer")
            return


    def handleTopVendite(self,e):
        self._view.txt_out.controls.clear()
        brand = self._view.ddBrand.value
        anno = self._view.ddAnno.value
        retailer = self._view.ddRetailer.value # retsituisce l'oggetto?
        # flag = False
        # if brand=="" and anno=="" and retailer=="":
        #     lista = self._model.getVenditeNoFiltri()
        #     flag = True
        #     lista.sort(key=operator.attrgetter('guadagno'), reverse=True)
        #     if len(lista)==0:
        #         self._view.txt_out.controls.append(ft.Text(f"non ci sono corssispondenze per anno: {anno}, brand: {brand} e retailer: {retailer}"))
        # elif brand is not None and anno is not None and retailer is not None:                                                                   # le altre combinazioni sono da fare?
        #     lista = self._model.getVendite(anno, brand, retailer)
        #     flag = True
        #     if len(lista)==0:
        #         self._view.txt_out.controls.append(ft.Text(f"non ci sono corssispondenze per anno: {anno}, brand: {brand} e retailer: {retailer}"))
        lista = self._model.getVenditeNoFiltri(anno, brand, retailer)
        lista.sort(key=operator.attrgetter('guadagno'), reverse=True)
        if len(lista) == 0:
            self._view.txt_out.controls.append(ft.Text(f"non ci sono corssispondenze per anno: {anno}, brand: {brand} e retailer: {retailer}"))
        else:
            for v in lista:
                self._view.txt_out.controls.append(ft.Text(f"{v}"))

            self._view._page.update()
            self._view.ddBrand.value =""
            self._view.ddAnno.value =""
            self._view.ddRetailer.value=""

    def handleAnalizzaVendite(self,e):
        self._view.txt_out.controls.clear()
        self.selezionaFiltri()
        brand = self._view.ddBrand.value
        anno = self._view.ddAnno.value
        retailer = self._view.ddRetailer.value

        res = self._model.AnalizzaVendite(anno, brand, retailer)
        self._view.txt_out.controls.append(ft.Text(f"Statistiche di vendita:\nGiro d'affari: {res[0]["guadagno"]}\nNumero vendite: {res[0]["quantitaTot"]}\nNumero retailer: {res[0]["numretailers"]}\nNumero prodotti: {res[0]["numProdDistinti"]}"))
        self._view._page.update()


    def fillDDAnno(self):
        annistr = self._model.getAnni()
        for a in annistr:
            self._view.ddAnno.options.append(ft.dropdown.Option(a))

    def fillDDBrand(self):
        brands = self._model.getBrand()
        for b in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(b))

    def fillDDRetailer(self):
        retailers = self._model.getRetailers()
        for r in retailers:
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=r.retailerCode, text=r,
                                                                    on_click=self.read_retailer))

    def read_retailer(self, e):
        self._retailer = e.control.data

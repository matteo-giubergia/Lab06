import operator

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleTopVendite(self,e):
        self._view.txt_out.controls.clear()
        brand = self._view.ddBrand.value
        anno = self._view.ddAnno.value
        retailer = self._view.ddRetailer.value # retsituisce l'oggetto?
        print(f"{brand} - {anno} - {retailer}")
        if brand=="Nessun filtro" and anno=="Nessun filtro" and retailer=="Nessun filtro":
            lista = self._model.getVenditeNoFiltri()
            lista.sort(key=operator.attrgetter('guadagno'), reverse=True)
        else:                                                                   # le altre combinazioni sono da fare?
            lista = self._model.getVendite(anno, brand, retailer)

        for v in lista:
            self._view.txt_out.controls.append(ft.Text(f"{v}"))
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

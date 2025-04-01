import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_out = None
        #dichiaro dropdown
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        #bottoni
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None



    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #inserisco dropdown
        self.ddAnno = ft.Dropdown(label="Anno", options=[ft.dropdown.Option("Nessun filtro")], width = 200)
        self._controller.fillDDAnno()

        self.ddBrand = ft.Dropdown(label="Brand", options=[ft.dropdown.Option("Nessun filtro")], width = 200)
        self._controller.fillDDBrand()

        self.ddRetailer = ft.Dropdown(label="Retailer", options=[ft.dropdown.Option("Nessun filtro")], width = 400)
        self._controller.fillDDRetailer()

        #inserisco bottoni
        self.btnTopVendite = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handleTopVendite, width = 200)
        self.btnAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", width = 200)

        #righe
        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self.btnTopVendite, self.btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        # List View
        self.txt_out = ft.ListView(expand=1)

        #aggiorna pagina
        self._page.add(row1, row2, self.txt_out)
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

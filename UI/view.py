import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.anno = None
        self.brand = None
        self.retailer = None
        self.btn_topVendite = None
        self.btn_analizzaVendite = None
        self.txt_result =None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self.anno = ft.Dropdown(label="anno", on_change=self._controller.handle_change_anno, width=300)
        self._controller.fillAnno()  # carica tutti i codici presi dal database

        self.brand = ft.Dropdown(label="brand", on_change=self._controller.handle_change_brand, width=300)
        self._controller.fillBrand()

        self.retailer = ft.Dropdown(label="retailer", width=300)


        row1 = ft.Row([self.anno, self.brand, self.retailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_topVendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_topVendite)
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_analizzaVendite)
        row2 = ft.Row([self.btn_topVendite, self.btn_analizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._page.controls.append(self.txt_result)
        self._page.update()

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

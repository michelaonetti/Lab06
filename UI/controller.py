import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None # Qui salviamo l'oggetto scelto


    def fillAnno(self):
        anni = self._model.get_anni()
        self._view.anno.options.append(ft.dropdown.Option(key="None", text="Nessun filtro")) #qui aggiung la scleta nessun filtro
        for a in anni:
            self._view.anno.options.append(ft.dropdown.Option(str(a)))
        self._view.update_page()

    def fillBrand(self):
        brands = self._model.get_brands()
        self._view.brand.options.append(ft.dropdown.Option(key="None", text="Nessun filtro"))
        for b in brands:
            self._view.brand.options.append(ft.dropdown.Option(b))
        self._view.update_page()

    def read_retailer(self, e):
        if e.control.data is None:
            self._retailer = None
        else:
            self._retailer = e.control.data
        print(f"Selezionato: {self._retailer}")

    def handle_change_anno(self, e):
        # Quando cambia l'anno, aggiorniamo i retailer
        self.aggiorna_retailer()

    def handle_change_brand(self, e):
        # Quando cambia il brand, aggiorniamo i retailer
        self.aggiorna_retailer()

    def aggiorna_retailer(self):
        lista_r = self._model.get_retailers() #restituisce una lista dei retails che equivalgono ai filtri di anno e brand messi

        # Svuota e ripopola il dropdown dei retailer con oggetti [cite: 77, 79]
        self._view.retailer.options = [ft.dropdown.Option(key="None", text="Nessun filtro")] #aggiungo al menu retailer , le vendite filtrate ottenute
        for r in lista_r:
            self._view.retailer.options.append(
                ft.dropdown.Option(
                    key=str(r.retailer_code),
                    text=r.retailer_name,
                    data=r,  # Passiamo l'oggetto intero della vendita
                    on_click=self.read_retailer  # Handler per la selezione
                )
            )


        self._view.update_page()



    def handle_topVendite(self,e):
        #cliccando qui mi stampo nel txt_result le migliori 5 vendite con quel anno, brand e retails.
        self._view.txt_result.controls.clear()
        anno = self._view.anno.value
        if anno == "Nessun filtro"or anno == "None" or anno is None:
            anno = None
        brand = self._view.brand.value
        if brand == "Nessun filtro" or brand == "None" or brand is None:
            brand = None
        retail = self._view.retailer.value
        if retail == "Nessun filtro"or brand == "None" or brand is None:
            retail = None

        risultati = self._model.getTopVendite(anno,brand, retail)

        for result in risultati:
            self._view.txt_result.controls.append(ft.Text(result.__str__()))
        self._view.update_page()

    def handle_analizzaVendite(self,e):
        """
        Considera solamente le vendite che soddisfano i filtri inseriti dall’utente. Deve stampare su
schermo le seguenti statistiche:
• Giro d’affari (ovvero volume totale dei ricavi)
• Numero di vendite
• Numero dei retailers coinvolti
• Numero di prodotti coinvolti
        """
        self._view.txt_result.controls.clear()
        anno = self._view.anno.value
        if anno == "Nessun filtro" or anno == "None" or anno is None:
            anno = None
        brand = self._view.brand.value
        if brand == "Nessun filtro" or brand == "None" or brand is None:
            brand = None
        retail = self._view.retailer.value
        if retail == "Nessun filtro" or brand == "None" or brand is None:
            retail = None

        risultati = self._model.getAnalizza(anno, brand, retail)

        self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari:{risultati[0]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vendite:{risultati[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di retails coinvolti:{risultati[2]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di prodotti coinvolti:{risultati[3]}"))
        self._view.update_page()


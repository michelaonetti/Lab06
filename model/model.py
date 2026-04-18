from database.DAO import DAO


class Model:
    def __init__(self):
        self._retailers = []
        self._MapVendite = {}
        self._brands = []
        self._anni = [] #i dati si aggioneranno la prima volta che farò la query, da quella volta in poi non ce ne sarà piu bisigon

#in questa classe controllo se ho gli element cercati del dizionario retails,
# altrimenti vado a chiamare il DAO
    def get_anni(self):
        if not self._anni:
            self._anni = DAO.getAllAnni()
        return self._anni

    def get_brands(self):
        if not self._brands:
            self._brands = DAO.getAllBrands()
        return self._brands

    def get_retailers(self):
        #sapendo anno e brand, mostro solo i retails di quell'anno e di prodotti di quel brand
        if not self._retailers:
            self._retailers = DAO.getAllRetailers()
        return self._retailers

    def getTopVendite(self,anno,brand,retail):
        return DAO.getTopVendite(anno, brand, retail)

    def getAnalizza(self,anno, brand, retail):
        return DAO.getAnalizza(anno,brand, retail)
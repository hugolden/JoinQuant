from joinQuant.DataModel.BaseFrame import BaseFrame

from joinQuant.DataModel.PriceCollection import PriceCollection


class CompanyFrame(BaseFrame):
    def __init__(self, context , frameId):
        super().__init__(context)
        self.__id = frameId
        self.__price_history = None

    def getPriceHistory(self):
        if(self.__price_history is None):
            self.__price_history = PriceCollection(self._context,self.__id)
        return self.__price_history.getPrices()




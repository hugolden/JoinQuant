from joinQuant.DataModel.BaseFrame import BaseFrame, DataQuery

from joinQuant.DataModel.PriceCollection import PriceCollection


class CompanyFrame(BaseFrame,DataQuery):
    def __init__(self, context , frameId):
        super().__init__(context)
        self.__id = frameId
        self.__price_history = None
        self.__fundamentals = {}

    def getPriceHistory(self):
        if(self.__price_history is None):
            self.__price_history = PriceCollection(self._context,self.__id)
        return self.__price_history.getPrices()

    def _queryFromMemory(self):

        return len(self.__fundamentals)!=0

    def _queryFromDatabase(self):
        return False

    def _queryFromServer(self):
        return False

    def executeQuery(self):
        super().executeQuery()





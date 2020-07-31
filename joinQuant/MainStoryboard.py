from joinQuant.Context import Context
from joinQuant.DataModel.ComaniesCollection import CompaniesCollection, CompaniesFundamentalCollection
from joinQuant.DataModel.Tables import TableManager


class MainStoryboard:
    def __init__(self):
        self.__context = Context()
        tableManager = TableManager(self.__context)
        tableManager.create_table()


    def getHightestHistoryDiff(self):
        pass

    def readCompaniesFromDatabase(self):
        pass

    def readCompaniesFromCache(self):
        pass

    def readCompaniesFromServer(self):
        pass

    def getAllCompaniesInfo(self):
        companiesCollection = CompaniesCollection(self.__context)
        companiesInfo = companiesCollection.executeQuery()

        fundamentalsCollection = CompaniesFundamentalCollection(self.__context)
        fundamentals = fundamentalsCollection.executeQuery()






import jqdatasdk as sdk

from joinQuant.Context import Context
from joinQuant.DataModel.ComaniesCollection import CompaniesCollection
from joinQuant.DataModel.CompanyFrame import CompanyFrame
from joinQuant.DataModel.Tables import TableManager


class DataContainer:
    def __init__(self):
        self.__context = Context()
        tableManager = TableManager(self.__context)
        tableManager.create_table()
        self.__companiesCollection = CompaniesCollection(self.__context)
        self.__companies = self.__companiesCollection.getCompanies()

    def getCompanies(self):
        return self.__companies


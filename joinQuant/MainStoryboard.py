from joinQuant.Context import Context
from joinQuant.DataModel.CompaniesCollection import CompaniesCollection, CompaniesFundamentalCollection, FundamentalEnum
from joinQuant.DataModel.Tables import TableManager


class MainStoryboard:
    def __init__(self):
        self.__context = Context()
        tableManager = TableManager(self.__context)
        tableManager.create_table()
        self.__companies = None
        self.__fundamentals = None

        self.__filteredFundatmentals = []


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
        self.__companies = companiesCollection.executeQuery()

        fundamentalsCollection = CompaniesFundamentalCollection(self.__context)
        self.__fundamentals = fundamentalsCollection.executeQuery()



    def findCompaniesROEGreaterThan15Percent(self):
        filteredCompanies = []
        for fundamental in self.__fundamentals:
            pe = fundamental[FundamentalEnum.pe_ratio.name]
            pb = fundamental[FundamentalEnum.pb_ratio.name]

            roe = pb/pe

            if roe >=0.4:
                code = fundamental[FundamentalEnum.code.name]
                filteredCompanies.append(code)
                print(code)

        print("Total for %r" %(len(filteredCompanies)))
        return filteredCompanies
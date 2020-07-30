import json
import os
from enum import Enum

from joinQuant.DataModel.BaseFrame import BaseFrame
from joinQuant.DataModel.BaseFrame import DataQuery
import jqdatasdk as sdk
import joinQuant.Database.CacheAgent as Cache

from joinQuant.DataModel.CompanyFrame import CompanyFrame
from joinQuant.Database import TableOperator


class CompaniesCollection(BaseFrame,DataQuery):
    TABLE = "CompaniesCollection"
    def __init__(self, context):
        super().__init__(context)
        self.__companies= []

        self.__attributes = [
            CompanyEnum.code,
            CompanyEnum.display_name,
            CompanyEnum.name,
            CompanyEnum.start_date,
            CompanyEnum.end_date,
            CompanyEnum.type
        ]


    def _queryFromMemory(self):
        return len(self.__companies) != 0

    def _queryFromDatabase(self):
        companies = self.__query_table()
        if len(companies==0):
            return False
        else:
            for singleQueryRow in companies:
                company = {}
                for attribute in self.__attributes:
                    company[attribute.name] = singleQueryRow[attribute.value]
                self.__companies.append(company) # add to memory
            return True

    def _queryFromServer(self):
        stockList = sdk.get_all_securities(types=['stock'])
        for index,row in stockList.iterrows():
            code =index
            attrSize = len(self.__attributes)
            values = [None]*attrSize
            values[0] = code
            company = {}
            company[CompanyEnum.code.name] = code
            for i in range(1,attrSize):
                company[self.__attributes[i].name] = row[self.__attributes[i].name]

            self.__insert_company(company) # add to database

            self.__companies.append(values) # add to memory

    def _executeQuery(self):
        super().executeQuery()


    def __query_table(self):

        companies = TableOperator.queryData(self._context, CompaniesCollection.TABLE)

        return companies

    def __insert_company(self,company:dict):
        TableOperator.insertData(self._context,CompaniesCollection.TABLE,company)
        return True

    def __query_cache(self):
        return Cache.readCompaniesFromCache()



class CompanyEnum(Enum):
    code = 0
    display_name = 1
    name = 2
    start_date = 3
    end_date = 4
    type = 5
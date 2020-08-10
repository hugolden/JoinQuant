from enum import Enum

import jqdatasdk as sdk

import joinQuant.Database.CacheAgent as Cache
from joinQuant import Utils
from joinQuant.DataModel.BaseFrame import BaseFrame
from joinQuant.DataModel.BaseFrame import DataQuery
from joinQuant.Database import TableOperator

from jqdatasdk import valuation, query


class CompaniesCollection(BaseFrame, DataQuery):
    TABLE = "CompaniesCollection"

    def __init__(self, context):
        super().__init__(context)
        self.__companies = []

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
        if len(companies) == 0:
            return False
        else:
            for singleQueryRow in companies:
                company = {}
                for attribute in self.__attributes:
                    company[attribute.name] = singleQueryRow[attribute.value]
                self.__companies.append(company)  # add to memory
            return True

    def _queryFromServer(self):
        stockList = sdk.get_all_securities(types=['stock'])
        for index, row in stockList.iterrows():
            code = index
            attrSize = len(self.__attributes)
            values = [None] * attrSize
            values[0] = code
            company = {}
            company[CompanyEnum.code.name] = code
            for i in range(1, attrSize):
                company[self.__attributes[i].name] = row[self.__attributes[i].name]

            self.__insert_company(company)  # add to database
            print(company)

            self.__companies.append(values)  # add to memory

    def executeQuery(self):
        super().executeQuery()
        return self.__companies

    def __query_table(self):

        companies = TableOperator.queryData(self._context, CompaniesCollection.TABLE)

        return companies

    def __insert_company(self, company: dict):
        TableOperator.insertData(self._context, CompaniesCollection.TABLE, company)
        return True

    def __query_cache(self):
        return Cache.readCompaniesFromCache()


class CompaniesFundamentalCollection(BaseFrame, DataQuery):
    TABLE = "Fundamental"

    def __init__(self, context):
        """
        class FundamentalEnum(Enum):
            code = 0
            day = 1
            capitalization = 3  # 总股本
            circulating_cap = 4  # 流通股本
            market_cap = 5  # 总市值
            circulating_market_cap = 6  # 流通市值
            turnover_ratio = 7  # 换手率
            pe_ratio = 8  # 动态市盈率
            pe_ratio_lyr = 9  # 静态市盈率
            pb_ratio = 10  # 市净率
            ps_ratio = 11  # 市销率
            pcf_ratio = 12  # 市现率
        """
        super().__init__(context)
        self.__fundamentals = []
        self.__attributes = [
            FundamentalEnum.code,
            FundamentalEnum.day,
            FundamentalEnum.capitalization,
            FundamentalEnum.circulating_cap,
            FundamentalEnum.market_cap,
            FundamentalEnum.circulating_market_cap,
            FundamentalEnum.turnover_ratio,
            FundamentalEnum.pe_ratio,
            FundamentalEnum.pe_ratio_lyr,
            FundamentalEnum.pb_ratio,
            FundamentalEnum.ps_ratio,
            FundamentalEnum.pcf_ratio
        ]

    def _queryFromMemory(self):
        return len(self.__fundamentals) != 0

    def _queryFromDatabase(self):
        today = Utils.get_today()
        yesterday = Utils.get_yesterday()
        fundamentals = TableOperator.queryData(self._context, CompaniesFundamentalCollection.TABLE,{FundamentalEnum.day.name:today})
        if len(fundamentals) == 0:
            fundamentals = TableOperator.queryData(self._context, CompaniesFundamentalCollection.TABLE,{FundamentalEnum.day.name:yesterday})
            if len(fundamentals) ==0:
                return False
        if (fundamentals[0][FundamentalEnum.day.value] == today or
                fundamentals[0][FundamentalEnum.day.value] == yesterday):
            self.__delete_data()
            return False
        for fundamentalRet in fundamentals:
            fundamental = {}
            for attribute in self.__attributes:
                fundamental[attribute.name] = fundamentalRet[attribute.value]
            self.__fundamentals.append(fundamental)

        return True

    def _queryFromServer(self):
        fundamentalQuery = self.__build_fundamentals_query()
        fundamentals = sdk.get_fundamentals(fundamentalQuery)
        for index, row in fundamentals.iterrows():
            fundamental = {}
            for attribute in self.__attributes:
                fundamental[attribute.name] = row[attribute.name]
            TableOperator.insertData(self._context, CompaniesFundamentalCollection.TABLE, fundamental)
            self.__fundamentals.append(fundamental)
            print(fundamental)

    def executeQuery(self):
        super().executeQuery()
        return self.__fundamentals

    def __delete_data(self):
        TableOperator.deleteFromTable(CompaniesFundamentalCollection.TABLE)

    def __build_fundamentals_query(self):
        q = query(valuation.code,
                  valuation.day,
                  valuation.capitalization,
                  valuation.circulating_cap,
                  valuation.market_cap,
                  valuation.circulating_market_cap,
                  valuation.turnover_ratio,
                  valuation.pe_ratio,
                  valuation.pe_ratio_lyr,
                  valuation.pb_ratio,
                  valuation.ps_ratio,
                  valuation.pcf_ratio,
                  )

        return q


class CompanyEnum(Enum):
    code = 0
    display_name = 1
    name = 2
    start_date = 3
    end_date = 4
    type = 5


class FundamentalEnum(Enum):
    code = 0
    day = 1
    capitalization = 2  # 总股本
    circulating_cap = 3  # 流通股本
    market_cap = 4  # 总市值
    circulating_market_cap = 5  # 流通市值
    turnover_ratio = 6  # 换手率
    pe_ratio = 7  # 动态市盈率
    pe_ratio_lyr = 8  # 静态市盈率
    pb_ratio = 9  # 市净率
    ps_ratio = 10  # 市销率
    pcf_ratio = 11  # 市现率

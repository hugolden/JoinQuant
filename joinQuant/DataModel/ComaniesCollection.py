from joinQuant.DataModel.BaseFrame import BaseFrame
import jqdatasdk as sdk

from joinQuant.DataModel.CompanyFrame import CompanyFrame


class CompaniesCollection(BaseFrame):
    def __init__(self, context):
        super().__init__(context)
        self.__companies=[]


    def getCompanies(self):
        if len(self.__companies)!=0:
            return self.__companies
        companies = self.__query_table()
        if len(companies) == 0:
            stockList = sdk.get_all_securities(types=['stock'])
            codes = stockList.index
            for code in codes:
                company = stockList.loc[[code]]
                self.__insert_company(code, company.display_name[0])
                companyFrame = CompanyFrame(self._context, code)
                self.__companies.append(companyFrame)
            self._cursor.commit()
        else:
            for companyTuple in companies:
                code = companyTuple[1]
                name = companyTuple[2]
                companyFrame = CompanyFrame(self._context,code)
                self.__companies.append(companyFrame)
        return self.__companies


    def __query_table(self):
        query_sql = "SELECT * FROM CompaniesCollection"

        self._cursor.execute(query_sql)

        companies = self._cursor.fetchall()
        return companies

    def __insert_company(self,code, name):
        insert_sql = "INSERT INTO CompaniesCollection (code,name) VALUES(%s,%s)"
        self._cursor.execute(insert_sql,(code,name))
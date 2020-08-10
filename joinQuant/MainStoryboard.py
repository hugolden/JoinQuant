from joinQuant import Utils
from joinQuant.Context import Context
from joinQuant.DataModel.CompaniesCollection import CompaniesCollection, CompaniesFundamentalCollection, \
    FundamentalEnum, CompanyEnum
from joinQuant.DataModel.CompaniesSTInfo import CompaniesSTInfo
from joinQuant.DataModel.Tables import TableManager
import jqdatasdk as sdk


class MainStoryboard:
    def __init__(self):
        self.__context = Context()
        tableManager = TableManager(self.__context)
        tableManager.create_table()
        self.__companies = None
        self.__fundamentals = None

        self.__is_st_infos = None

        self.__filteredFundatmentals = []


    def getAllCompaniesInfo(self):
        companiesCollection = CompaniesCollection(self.__context)
        self.__companies = companiesCollection.executeQuery()

        fundamentalsCollection = CompaniesFundamentalCollection(self.__context)
        self.__fundamentals = fundamentalsCollection.executeQuery()


        codes = []
        for company in self.__companies:
            codes.append(company[CompanyEnum.code.name])

        st_infos = CompaniesSTInfo(self.__context,codes)
        self.__is_st_infos = st_infos.executeQuery()




    def findCompaniesROEGreaterThan15Percent(self):
        filteredCompanies = []
        for fundamental in self.__fundamentals:
            code = fundamental[FundamentalEnum.code.name]
            pe = fundamental[FundamentalEnum.pe_ratio.name]

            pe_lyr = fundamental[FundamentalEnum.pe_ratio_lyr.name]

            pb = fundamental[FundamentalEnum.pb_ratio.name]

            is_st = self.__is_st_infos[code]

            if is_st:
                continue

            roe = pb/pe

            accelerate  =pe_lyr/pe
            if pe<0:
                continue
            if accelerate<1:
                continue

            if roe >=0.15 :
                filteredCompanies.append(code)
                print(code)



        print("Total filtered non-st companies:%r" %(len(filteredCompanies)))

        return filteredCompanies



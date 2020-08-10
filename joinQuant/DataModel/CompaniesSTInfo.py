from enum import Enum

from joinQuant import Utils
from joinQuant.DataModel.BaseFrame import BaseFrame, DataQuery
from joinQuant.Database import TableOperator

import jqdatasdk as sdk


class CompaniesSTInfo(BaseFrame, DataQuery):
    TABLE = "STInfo"

    def __init__(self, context, companies):
        super().__init__(context)
        self.__companies = companies
        self.__companies_st = {}
        self.__attributes = {
            CompaniesSTEnum.code,
            CompaniesSTEnum.is_st,
            CompaniesSTEnum.last_edit_time
        }

        pass

    def _queryFromMemory(self):
        return len(self.__companies_st) != 0

    def _queryFromDatabase(self):
        data_queried = TableOperator.queryData(self._context, CompaniesSTInfo.TABLE)
        if len(data_queried) == 0:
            return False
        edit_date = data_queried[0][CompaniesSTEnum.last_edit_time.value]
        if Utils.get_today()!=edit_date :
            TableOperator.deleteFromTable(self._context, CompaniesSTInfo.TABLE)
            return False
        for row in data_queried:
            self.__companies_st[row[CompaniesSTEnum.code.value]] = row[CompaniesSTEnum.is_st.value]
        return True

    def _queryFromServer(self):
        is_st_infos = sdk.get_extras('is_st', self.__companies, start_date=Utils.get_yesterday(),
                                     end_date=Utils.get_today(),
                                     df=True)
        st_info_serials = is_st_infos.iloc[0]




        today = Utils.get_today()
        for index, value in st_info_serials.items():
            self.__companies_st[index] = value
            entry = {}
            entry[CompaniesSTEnum.code.name] = index
            entry[CompaniesSTEnum.is_st.name] = value
            entry[CompaniesSTEnum.last_edit_time.name] = today
            TableOperator.insertData(self._context, CompaniesSTInfo.TABLE, entry=entry)


    def executeQuery(self):
        super().executeQuery()
        return self.__companies_st


class CompaniesSTEnum(Enum):
    code = 0
    is_st = 1
    last_edit_time = 2

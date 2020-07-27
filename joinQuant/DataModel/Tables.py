from joinQuant.DataModel.BaseFrame import BaseFrame


class TableManager(BaseFrame):
    def __init__(self,context):
        super().__init__(context)

    def create_table(self):
        create_company_table_sql = "CREATE TABLE IF NOT EXISTS CompaniesCollection(" \
                           "    ID SERIAL PRIMARY KEY," \
                           "    code varchar(12)," \
                           "    name varchar(100)" \
                           ")"

        create_dates_table_sql = "CREATE TABLE IF NOT EXISTS PriceCollection(" \
                                 "    ID SERIAL PRIMARY KEY," \
                                 "    companyCode varchar(12)," \
                                 "    dateStr  varchar(32)" \
                                 ")"

        create_prices_table_sql = " CREATE TABLE IF NOT EXISTS  Price(" \
                                  "    priceId BIGSERIAL PRIMARY KEY," \
                                  "    companyCode varchar(12)," \
                                  "    date varchar(32)," \
                                  "    openPrice double precision," \
                                  "    closePrice double precision," \
                                  "    highPrice double precision," \
                                  "    lowPrice double precision" \
                                  ") "

        self._cursor.execute(create_company_table_sql)
        self._cursor.execute(create_dates_table_sql)
        self._cursor.execute(create_prices_table_sql)
        self._cursor.commit()



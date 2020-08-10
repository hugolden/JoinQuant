from joinQuant.DataModel.BaseFrame import BaseFrame


class TableManager(BaseFrame):
    def __init__(self,context):
        super().__init__(context)

    def create_table(self):
        create_company_table_sql = "CREATE TABLE IF NOT EXISTS CompaniesCollection(" \
                           "    ID SERIAL PRIMARY KEY," \
                           "    code varchar(12)," \
                           "    display_name varchar(32)," \
                           "    name varchar(100)," \
                           "    start_date varchar(32)," \
                           "    end_date varchar(32)," \
                           "    type varchar(32)," \
                           "    last_edit_date varchar(32)" \
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

        create_fundamentals_table_sql = "CREATE TABLE IF NOT EXISTS Fundamental(" \
                                        "code varchar(12) PRIMARY KEY," \
                                        "day varchar(32)," \
                                        "capitalization double precision," \
                                        "circulating_cap double precision," \
                                        "market_cap double precision," \
                                        "circulating_market_cap double precision," \
                                        "turnover_ratio double precision," \
                                        "pe_ratio double precision," \
                                        "pe_ratio_lyr double precision," \
                                        "pb_ratio double precision," \
                                        "ps_ratio double precision," \
                                        "pcf_ratio double precision" \
                                        ")"

        create_company_st_table_sql = "CREATE TABLE IF NOT EXISTS STInfo(" \
                                      "code varchar(12) PRIMARY KEY," \
                                      "is_st boolean," \
                                      "last_edit_time varchar(32)" \
                                      ")"

        self._cursor.execute(create_company_table_sql)
        self._cursor.execute(create_dates_table_sql)
        self._cursor.execute(create_prices_table_sql)
        self._cursor.execute(create_fundamentals_table_sql)
        self._cursor.execute(create_company_st_table_sql)
        self._cursor.commit()



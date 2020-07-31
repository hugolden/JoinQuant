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
                           "    type varchar(32)" \
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

        create_fundamentals_table_sql = "CREATE TABLE IF NO EXISTS Fundamental(" \
                                        "code varchar(12) PRIMARY KEY," \
                                        "date varchar(32)," \
                                        "capitalization double precision," \
                                        "circulating_cap double precision," \
                                        "market_cap double prcision," \
                                        "circulating_market_cap double prcision," \
                                        "turnover_ratio double prcision," \
                                        "pe_ratio double prcision," \
                                        "pe_ratio_lyr double prcision," \
                                        "pb_ratio double prcision," \
                                        "ps_ratio double prcision," \
                                        "pcf_ratio double prcision" \
                                        ")"

        self._cursor.execute(create_company_table_sql)
        self._cursor.execute(create_dates_table_sql)
        self._cursor.execute(create_prices_table_sql)
        self._cursor.execute(create_fundamentals_table_sql)
        self._cursor.commit()



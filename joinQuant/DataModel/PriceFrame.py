from joinQuant.DataModel.BaseFrame import BaseFrame


class PriceFrame(BaseFrame):
    def __init__(self, context,companyCode,dateStr):
        super().__init__(context)
        self.__date = dateStr
        self.__companyCode = companyCode
        self.__openPrice = None
        self.__closePrice = None
        self.__highPrice = None
        self.__lowPrice = None
        self.__isPersisted = False

    def persistPrice(self,dailyPrice):
        self.__openPrice = dailyPrice.openPrice
        self.__closePrice = dailyPrice.closePrice
        self.__highPrice = dailyPrice.highPrice
        self.__lowPrice = dailyPrice.lowPrice
        self.__insert_date(dailyPrice.openPrice,dailyPrice.closePrice,dailyPrice.highPrice,dailyPrice.lowPrice)
        pass

    def getPrice(self):
        return self.__query()


    def __str__(self):
        return "code is {5}, date is {4}, open is {0}, close is {1}, high is {2}, low is {3}".format(self.__openPrice,self.__lowPrice,self.__highPrice,self.__lowPrice,self.__date,
                                                                                                     self.__companyCode)

    def __query(self):
        get_price_sql = "SELECT * FROM Price WHERE date=%s AND companyCode=%s"

        self._cursor.execute(get_price_sql,(self.__date,self.__companyCode))

        price = self._cursor.fetchone()
        if price is not None:
            self.__openPrice =price[3]
            self.__closePrice=price[4]
            self.__highPrice = price[5]
            self.__lowPrice = price[6]
            # price = DailyPrice(self.__openPrice,self.__closePrice,self.__highPrice,self.__lowPrice)
        return self





    def __insert_date(self,open_price,close_price,high_price,low_price):
        insert_data_sql = "INSERT INTO Price (companyCode, date, openPrice, closePrice, highPrice,lowPrice) VALUES (%s,%s,%s,%s,%s,%s)"
        self._cursor.execute(insert_data_sql,[self.__companyCode,self.__date,open_price,close_price,high_price,low_price])
        pass


class DailyPrice:
    def __init__(self, openPrice , closePrice, highPrice, lowPrice):
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.highPrice = highPrice
        self.lowPrice = lowPrice
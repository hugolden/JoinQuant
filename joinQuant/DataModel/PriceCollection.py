from joinQuant.DataModel.BaseFrame import BaseFrame
import jqdatasdk as sdk

from joinQuant.DataModel.PriceFrame import PriceFrame, DailyPrice


class PriceCollection(BaseFrame):
    def __init__(self,context, companycode):
        super().__init__(context)
        self.__prices={}
        self.__companyCode =companycode


    def __query_date_collection(self):
        query_dates = "SELECT * FROM PriceCollection WHERE companyCode= %s"
        self._cursor.execute(query_dates,[self.__companyCode])
        dates= self._cursor.fetchall()
        return dates


    def __insert_date_collection(self,dateStr):
        insert_dates = "INSERT INTO PriceCollection (companyCode, dateStr) VALUES(%s, %s)"
        self._cursor.execute(insert_dates,(self.__companyCode,dateStr))

    def getPrices(self):
        if len(self.__prices)!=0:
            return self.__prices
        dates = self.__query_date_collection()
        if len(dates) ==0:
            frames = sdk.get_price(self.__companyCode, start_date='2018-01-01 10:00:00', end_date='2019-01-01 10:00:00',
                                   frequency='daily', panel=False)
            indices = frames.index



            for index in indices:
                self.__insert_date_collection(index)
                singleFrame = frames.loc[index]
                price = PriceFrame(self._context, self.__companyCode, index)
                self.__prices[self.__companyCode] = price
                dailyPrice = DailyPrice(singleFrame.open, singleFrame.close, singleFrame.high, singleFrame.low)
                price.persistPrice(dailyPrice=dailyPrice)

            self._cursor.commit()
        else:
            for date in dates:
                dateStr = date[2]
                price = PriceFrame(self._context, self.__companyCode,dateStr)
                price.getPrice()
                print(price)
                self.__prices[self.__companyCode] = price

        print('get price from '+self.__companyCode)
        return self.__prices


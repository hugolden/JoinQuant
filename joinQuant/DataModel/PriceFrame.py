class PriceFrame:
    def __init__(self, dateStr, **price):
        self.__date = price['timestamp']
        self.__openPrice = price['open']
        self.__closePrice = price['close']
        self.__highPrice = price['high']
        self.__lowPrice = price['low']


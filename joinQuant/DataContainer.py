import jqdatasdk as sdk

class DataContainer:
    def __init__(self):
        self.__stockList = []


    def updateList(self):
        self.__stockList = sdk.get_all_securities(types=['stock','fund'])
        print(self.__stockList)

    def updateAllData(self):
        return False # update failed

    def getSingleFrame(self, secId):
        pass
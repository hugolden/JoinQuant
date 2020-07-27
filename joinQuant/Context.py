from joinQuant.Database.DatabaseAgent import DBCusorProxy


class Context:
    def __init__(self):
        self.__cusor = None

    def getCusor(self):
        if self.__cusor == None:
            self.__cusor = DBCusorProxy()

        return self.__cusor

    def finalize(self):
        self.__cusor.finalize()

import psycopg2 as psy

from joinQuant import Config


class DBCusorProxy:
    def __init__(self):
        dbName = Config.DATABASE
        usr = Config.USER
        pwd = Config.PASSWORD
        host = Config.HOST
        port = Config.PORT
        self.__connection = psy.connect(database=dbName, user=usr, password=pwd, host=host, port=port)
        self.__alive = True
        self.__cursor = self.__connection.cursor()

    def execute(self, sqlStr, vars=None):
        if self.__alive:
            self.__cursor.execute(sqlStr, vars)

    def commit(self):
        if self.__alive:
            self.__connection.commit()

    def fetchone(self):
        if self.__alive:
            return self.__cursor.fetchOne()

        return None

    def fetchall(self):
        if self.__alive:
            return self.__cursor.fetchall()
        return None

    def fetchmany(self, outArray):
        if self.__alive:
            return self.__cursor.fetchmany(outArray)
        return None

    def commit(self):
        if self.__alive:
            self.__connection.commit()

    def rollback(self):
        if self.__alive:
            self.__cursor.rollback()

    def rowCount(self):
        if self.__alive:
            return self.__cursor.rowcount()
        return 0

    def finalize(self):
        self.__alive = False
        self.__cursor.close()
        self.__connection.close()
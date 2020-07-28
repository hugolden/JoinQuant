import abc


class BaseFrame:

    def __init__(self, context):
        self._context = context
        self._cursor = context.getCusor()


class DataQuery(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def queryFromMemory(self):
        pass

    @abc.abstractmethod
    def queryFromDatabase(self):
        pass

    @abc.abstractmethod
    def queryFromCache(self):
        pass

    @abc.abstractmethod
    def queryFromServer(self):
        pass

    def executeQuery(self):
        if not self.queryFromMemory():
            if not self.queryFromDatabase():
                if not self.queryFromCache():
                    self.queryFromServer()

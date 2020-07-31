import abc


class BaseFrame:

    def __init__(self, context):
        self._context = context
        self._cursor = context.getCusor()


class DataQuery(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def _queryFromMemory(self):
        pass

    @abc.abstractmethod
    def _queryFromDatabase(self):
        pass


    @abc.abstractmethod
    def _queryFromServer(self):
        pass

    def executeQuery(self):
        if not self._queryFromMemory():
            if not self._queryFromDatabase():
                self._queryFromServer()

class BaseFrame:

    def __init__(self, context):
        self._context = context
        self._cursor = context.getCusor()

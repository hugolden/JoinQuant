from joinQuant.Context import Context


def queryData(context: Context, tableName: str, params: dict = {}) -> list:
    query_sql = "SELECT * FROM {}".format(tableName)
    cursor = context.getCusor()
    if len(params) != 0:
        query_sql += " WHERE "
        items = list(params.items())
        values = []
        for i in range(len(items)):
            key = items[i][0]
            value = items[i][1]
            values.append(value)
            query_sql += key + "=%s"
            if i != (len(items) - 1):
                query_sql += " AND "
        cursor.execute(query_sql,values)

    else:
        cursor.execute(query_sql)
    result = cursor.fetchall()
    return result


def deleteFromTable(context:Context, tableName:str, conditions:dict = {}):
    delete_sql = "DELETE FROM {}".format(tableName)
    cursor = context.getCusor()
    items = list(conditions.items())
    size = len(items)
    if size>0:
        condition = " WHERE "
        values = []
        for i in range(size):
            item = items[i]
            condition += "{0}={1}".format(item[0],"%s")
            values.append(item[1])
            if i == size-1:
                condition+=" AND "
        delete_sql+=condition
        cursor.execute(delete_sql, tuple(values))
    else:
        cursor.execute(delete_sql)
    cursor.commit()

    pass




def insertData(context: Context, tableName: str, entry: dict):
    insert_sql = "INSERT INTO {} (".format(tableName)

    items = list(entry.items())
    values = []
    valuesHolder = "("
    size = len(items)
    for i in range(size):
        insert_sql += items[i][0]
        values.append(items[i][1])
        valuesHolder += "%s"
        if i != size - 1:
            insert_sql += ','
            valuesHolder += ','
        else:
            insert_sql += ')'
            valuesHolder += ')'

    insert_sql = "{0} VALUES {1}".format(insert_sql, valuesHolder)

    cursor = context.getCusor()
    cursor.execute(insert_sql, tuple(values))
    cursor.commit()
    return

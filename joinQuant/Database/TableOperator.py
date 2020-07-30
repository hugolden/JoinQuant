from joinQuant.Context import Context


def queryData(context: Context, tableName: str, params: dict = {}) -> list:
    query_sql = "SELECT * FROM %s".format(tableName)
    if len(dict) != 0:
        query_sql += "WHERE"
        items = list(params)
        for i in range(len(items)):
            key = items[i][0]
            value = items[i][1]
            query_sql += key + "=" + value
            if i != (len(items) - 1):
                query_sql += " AND "

    cursor = context.getCusor()
    cursor.execute(query_sql)
    result = cursor.fetchall()
    return result


def insertData(context: Context, tableName: str, entries: dict):
    insert_sql = "INSERT INTO %s (".format(tableName)

    items = list(entries.items())
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

    insert_sql = "%s VALUES %s".format(insert_sql, valuesHolder)

    cursor = context.getCusor()
    cursor.execute(insert_sql, tuple(values))
    return

#coding=utf-8
#coding=gbk
import datetime
import json
import os


def getTimeStamp():
    return '%s' % (datetime.date.today())

def writeCompaniesToCache(stockList):
    companiesDict = {}
    companies = []
    companiesDict['companies'] = companies
    companiesDict['timestamp'] = datetime
    codes = stockList.index
    for code, companySlice in codes:
        companyFrame = {}
        companyFrame['code'] = code
        companyFrame['display_name']= companySlice['display_name']
        companyFrame['name'] = companySlice['name']
        companyFrame['start_date'] = companySlice['start_date']
        companyFrame['end_date'] = companySlice['end_date']
        companyFrame['type'] = companySlice['type']
        companies.append(companyFrame)

    serializedCompanies = json.dump(companiesDict)

    path = os.path.join(".", "Cache", "companies.txt")

    with open(path,'rw', encoding='utf-8') as f:
        f.write(serializedCompanies)


def readCompaniesFromCache():
    path = os.path.join(".", "Cache", "companies.txt")
    if not os.path.exists(path):
        return None
    with open(path,"rw",encoding='utf-8') as f:
        jsonStr = f.read()
        jsonObj = json.loads(jsonStr)
        if jsonObj.has_key('timestamp'):
            timestamp = jsonObj['timestamp']
            if timestamp != getTimeStamp():
                return None
            return jsonObj
        return None




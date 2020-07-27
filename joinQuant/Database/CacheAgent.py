import json

def writeCompaniesToCache(stockList):
    companiesDict = {}
    companies = []
    companiesDict['companies'] = companies
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

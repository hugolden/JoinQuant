import jqdatasdk as sdk
import pandas as pd

from joinQuant.DataContainer import DataContainer
from joinQuant.DataModel.Tables import TableManager


def auth():
    sdk.auth('18018517267','517267')


if __name__ == '__main__':
    auth()
    container = DataContainer()
    companies = container.getCompanies()
    for company in companies:
        priceHistory = company.getPriceHistory()


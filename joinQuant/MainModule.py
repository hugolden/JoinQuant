import jqdatasdk as sdk
import pandas as pd

from joinQuant.DataContainer import DataContainer


def auth():
    sdk.auth('18018517267','517267')


if __name__ == '__main__':
    auth()
    container = DataContainer()
    container.updateList()

import jqdatasdk as sdk

from joinQuant.MainStoryboard import MainStoryboard


def auth():
    sdk.auth('18018517267','517267')


if __name__ == '__main__':
    auth()
    storyBoard = MainStoryboard()
    storyBoard.getAllCompaniesInfo()


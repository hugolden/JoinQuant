from datetime import date
from datetime import timedelta

def get_yesterday():
    yesterday = date.today()-timedelta(1)
    return '%s' %(yesterday)

def get_today():
    return '%s' %(date.today())
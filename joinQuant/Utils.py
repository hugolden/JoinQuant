from datetime import date
from datetime import timedelta

def get_yesterday():
    yesterday = date.today()-timedelta(1)
    return '%s' %(yesterday)

def get_today():
    return '%s' %(date.today())

def get_last_year():
    lastYear = (date.today()-timedelta(365)).year
    return "%s" %(lastYear)

def get_this_year():
    return "%s" %(date.today().year)
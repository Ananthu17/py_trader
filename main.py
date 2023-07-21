from py5paisa import FivePaisaClient
from py5paisa.order import Order, OrderType, Exchange
import requests
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import time
from decouple import config

# Load variables from the .env file
APP_NAME = config('APP_NAME')
APP_SOURCE = config('APP_SOURCE')
USER_ID = config('USER_ID')
PASSWORD = config('PASSWORD')
USER_KEY = config('USER_KEY')
ENCRYPTION_KEY = config('ENCRYPTION_KEY')

cred = {
    "APP_NAME": APP_NAME,
    "APP_SOURCE": APP_SOURCE,
    "USER_ID": USER_ID,
    "PASSWORD": PASSWORD,
    "USER_KEY": USER_KEY,
    "ENCRYPTION_KEY": ENCRYPTION_KEY
}

# Login
client = FivePaisaClient(email=config('EMAIL'), passwd=config('PASSWD'),
                         dob=config('DOB'), cred=cred)
client.login()

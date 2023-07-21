from py5paisa import FivePaisaClient
from decouple import config
from info import Info
from order import Order

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

market_info = Info(client)
order = Order(client)

print(market_info.get_market_status())

import requests
import sys


try:
    y = float(sys.argv[1])
    print(y)
except ValueError:
    sys.exit("error")


headers = requests.headers("https://api.coindesk.com/v1/bpi/currentprice.json")

print(headers)

# response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# o = response.json()
# for result in o["USD"]:
#    print(result["rate_float"])

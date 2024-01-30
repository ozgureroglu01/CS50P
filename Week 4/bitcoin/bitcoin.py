import sys
import requests


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = response.json()
    bitcoin_value = bitcoin["bpi"]["USD"]["rate_float"]
    amount = bitcoin_value * number
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

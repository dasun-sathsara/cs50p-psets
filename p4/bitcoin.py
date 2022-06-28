import requests
import json
import sys

try:
    assert len(sys.argv) == 2
    bitcoins = float(sys.argv[1])
except AssertionError:
    print("wrong number of arguements")
    sys.exit()
except ValueError:
    print("bad arguement")
    sys.exit()


try:
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")
    response_dict = json.loads(response.content)
except:
    print("something went wrong with the web request")
    sys.exit()


price = response_dict["bpi"]["USD"]["rate_float"]
total_price = price * bitcoins
print(f"Total Price: {total_price:,.4f}")

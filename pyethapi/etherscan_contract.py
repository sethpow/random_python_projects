import requests
from decimal import Decimal


address = "0x9674dF2b0E96d51A0c74a4725911aaD6C4B6F77C"
url = "https://api-kovan.etherscan.io/api?module=account&action=txlist&address=" + address + \
"&startblock=0&endblock=99999999&sort=asc&apikey=2FU5VXX8GINBITCEBX5J7I2EKJH4NP8JRR"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like


response = requests.get(url, headers=headers)
# print(response)
# print(response.status_code)
# print(response.url)
# print(response.content)

address_content = response.json()
# print(address_content)

# return only result from array
result = address_content.get("result")
# print(result)

for n, transaction in enumerate(result):
    data = {
        "id": n,
        "hash": transaction.get('hash'),
        "from": transaction.get('from'),
        "to": transaction.get('to'),
        "value": Decimal(transaction.get('value')) / Decimal('1000000000000000000'),
        "confirmations": transaction.get('confirmations'),
        "gasUsed": transaction.get("gasUsed") + ' wei'
    }

    print(data, "\n")
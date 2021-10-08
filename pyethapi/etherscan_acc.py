import os
import json
import requests
from decimal import Decimal
import certifi
from dotenv import load_dotenv
load_dotenv()


api = os.environ.get("API_KEY")


def input_address():
    _address = input("What is your address?\n")
    return _address


def get_transactions_by_address(_address):

    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + _address + \
    "&startblock=0&endblock=99999999&sort=asc&apikey=" + f"{api}"

    response = (requests.get(url, verify=certifi.where())).json()
    result = response.get("result")
    total_balance = 0;

    if len(result) == 1:
        print(f"\nWriting {len(result)} transaction to file")
    else:
        print(f"\nWriting {len(result)} transaction's to file")

    for n, tx in enumerate(result):
        data = {
            "tx_number": n + 1,
            "from": tx.get("from"),
            "to": tx.get("to"),
            "status": "OUT/Sent" if (tx.get("from") == _address.lower()) else "IN/Received",
            "value": float(tx.get("value")) / float("1000000000000000000"),
            "gas": tx.get("gas"),
            "gasPrice": tx.get("gasPrice"),
            "gasUsed": tx.get("gasUsed"),
            "contractAddress": tx.get("contractAddress"),
            "posted": bool(tx.get("txreceipt_status")),
            "confirmed": "Confirmed" if int(tx.get("confirmations")) >= 250 else "Pending",
            "confirmations": tx.get("confirmations")
        }

        # (total_balance) += int(tx.get("value")) / Decimal("1000000000000000000")


        # print("Balance: ", total_balance)

        # f = open("output.txt", 'a')
        # print(f"Writing {n + 1} transaction's to file...\n")

        with open(_address + ".txt", 'a') as output_file:
            output_file.write(json.dumps(data))
            output_file.write("\n")
            output_file.close()

        # f.write(data)
        # f.close()


    print("Creating file...\n")


get_transactions_by_address(input_address())
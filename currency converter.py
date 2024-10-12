"""currency converter"""

import requests

def main():
    """currency converter"""
    init_currency = input("Enter the initial currency: ")
    # Variable for recieve initial currency befor conversinon
    dem_currency = input("Enter the demand currency: ")
    # Variable for recieve demand currency after conversion

    amount = float(input("Enter the amount for converting: "))
    # Variable for recieve amount of initial currency for conversion

    # Request API from APIlayer.com (Keyword : Currency)
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={dem_currency}&from={init_currency}&amount={amount}"
    payload = {}
    headers= {"apikey": "XA1YOaGmzrmuqI8SI9DzmEnQzySi02KB"}

    response = requests.request("GET", url, headers = headers, data = payload)
    result = response.json()

    status_code = response.status_code
    if status_code == 200: # Condition for check Error from reponse then get result
        print("Conversion result: " + str(result["result"]))
    else:
        print("Error response: " + str(result["error"]))
        quit()

main()

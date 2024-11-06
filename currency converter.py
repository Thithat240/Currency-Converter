"""Currency Converter"""

import tradermadekey
import requests

#API Keys
api_key = tradermadekey.key

def convert_currency(amount, from_currency, to_currency):
    """Return rates and covert amount"""
    # Request rates from tradermade.com
    url = f"https://marketdata.tradermade.com/api/v1/convert?api_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        rate = response.json()["quote"]
        converted_amount = response.json()["total"]
        return rate, converted_amount
    else:
        return None, None

def currency_converter():
    """Currency converter application"""
    # Input amount
    amount = float(input())
    # Input 'from' currency
    from_currency = input()
    # Input 'to' currencies
    to_currency = input()
    # Check if the exchange pair is avaliable
    try:
        # Convert currency 
        rate, converted_amount = convert_currency(amount, from_currency, to_currency)
        # Check API is avaliable.
        if rate:
            # Display result
            return f"""Converted amount : {amount} {from_currency} = {converted_amount} {to_currency}
Conversion rate : {rate}"""
        else:
            return f"Something Went Wrong Please Check with your API Provider"
    except:
        return f"Error: Exchange rates not available for {from_currency} to {to_currency}."
    
print(currency_converter())

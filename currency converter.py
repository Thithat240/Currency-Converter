"""Currency Converter"""

import tradermadekey
import requests

#API Keys
api_key = tradermadekey.key

def fetch_supported_forex():
    """Return all currency pairs"""
    # Request exchange pairs from tradermade.com
    url = f"https://marketdata.tradermade.com/api/v1/live_currencies_list?api_key={api_key}"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        currencies_data = response.json()
        # Check if key is found
        if "available_currencies" in currencies_data:
            currencies = currencies_data["available_currencies"]
            return currencies
        else:
            return "Error: 'available_currencies' key not found in response."
    else:
        return f"Error {response.status_code}: {response.text}"
    
def fetch_supported_crypto():
    """Return all crypto pairs"""
    # Request exchange pairs from tradermade.com
    url = f"https://marketdata.tradermade.com/api/v1/live_crypto_list?api_key={api_key}"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        currencies_data = response.json()
        # Check if key is found
        if "available_currencies" in currencies_data:
            currencies = currencies_data["available_currencies"]
            return currencies
        else:
            return "Error: 'available_currencies' key not found in response."
    else:
        return f"Error {response.status_code}: {response.text}"

# print(fetch_supported_forex())
# supported_forex = {'AED': 'UAE Dirham', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'BAM': 'Bosnia and Herzegovina Conv Mark', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgaria Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BRL': 'Brazilian Real', 'BYN': 'Belarusian Ruble', 'CAD': 'Canadian Dollar', 'CHF': 'Swiss Franc', 'CLP': 'Chilean Peso', 'CNH': 'Chinese Yuan offshore', 'CNY': 'Chinese Yuan onshore', 'COP': 'Colombian Peso', 'CZK': 'Czech Koruna', 'DKK': 'Danish Krone', 'EGP': 'Egyptian Pound', 'EUR': 'Euro', 'GBP': 'British Pound Sterling', 'GHS': 'Ghanaian Cedi', 'HKD': 'Hong Kong Dollar', 'HRK': 'Croatian Kuna', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'INR': 'Indian Rupee', 'ISK': 'Icelandic Krona', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shillings', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KZT': 'Kazakhstani Tenge', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'MAD': 'Moroccan Dirham', 'MUR': 'Mauritian Rupee', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'NGN': 'Nigerean Naira', 'NOK': 'Norwegian Krone', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PEN': 'Peruvian Nuevo Sol', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RUB': 'Russian Ruble', 'SAR': 'Saudi Arabian Riyal', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'THB': 'Thai Baht', 'TND': 'Tunisian Dinar', 'TRY': 'Turkish Lira', 'TWD': 'Taiwanese Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'US Dollar', 'VND': 'Vietnamese Dong', 'XAF': 'Central African Francs', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XOF': 'West African CFA franc', 'XPD': 'Palladium', 'XPT': 'Platinum', 'ZAR': 'South African Rand', 'ZWL': 'Zimbabwean Dollar'}
# print(fetch_supported_crypto())
# supported_crypto = {'ADA': 'Cardano', 'ATOM': 'Atom', 'AVAX': 'Avalanche', 'AXS': 'Axis infinity', 'BCH': 'Bitcoin Cash', 'BNB': 'Binance Coin', 'BTC': 'Bitcoin', 'BTG': 'Bitcoin Gold', 'BUSD': 'Binance USD', 'DAI': 'DAI', 'DASH': 'Dashcoin', 'DOGE': 'DogeCoin', 'DOT': 'Polkadot', 'EGLD': 'Elrond Egold', 'ENJ': 'ENJ', 'EOS': 'EOS Platform', 'ETC': 'Ethereum Classic', 'ETH': 'Ethereum', 'FIL': 'Filecoin', 'FLOW': 'Flow', 'FTM': 'Fantom USD', 'FTT': 'FTX Token', 'GALA': 'Gala', 'HBAR': 'Hbar', 'HNT': 'Helium', 'ICP': 'Internet Computer Price ', 'LINK': 'Chainlink', 'LRC': 'Loopring', 'LTC': 'Litecoin', 'LUNA': 'Luna', 'MANA': 'Decentraland', 'MATIC': 'Matic', 'NEAR': 'Near', 'NEO': 'NEO', 'ROSE': 'Rose', 'SAND': 'Sandbox', 'SHIB': 'Shiba inu', 'SOL': 'Solana', 'THETA': 'Theta', 'TRX': 'Tron', 'UNI': 'Uniswap', 'USDT': 'Tether', 'UST': 'Terra USD', 'VET': 'Vechain', 'XLM': 'Stellar', 'XMR': 'Monero', 'XRP': 'Ripple', 'XTZ': 'Tezos'}

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

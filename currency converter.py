"""Currency Converter"""

import tradermadekey
import tkinter as tk
from tkinter import ttk, messagebox
import requests

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
        return None

# Forex and crypto pairs
pair={
    'AED': 'UAE Dirham', 
    'ALL': 'Albanian Lek', 
    'AMD': 'Armenian Dram', 
    'AOA': 'Angolan Kwanza', 
    'ARS': 'Argentine Peso', 
    'AUD': 'Australian Dollar', 
    'BAM': 'Bosnia and Herzegovina Conv Mark', 
    'BDT': 'Bangladeshi Taka', 
    'BGN': 'Bulgaria Lev', 
    'BHD': 'Bahraini Dinar', 
    'BIF': 'Burundian Franc', 
    'BRL': 'Brazilian Real', 
    'BYN': 'Belarusian Ruble', 
    'CAD': 'Canadian Dollar', 
    'CHF': 'Swiss Franc', 
    'CLP': 'Chilean Peso', 
    'CNH': 'Chinese Yuan offshore', 
    'CNY': 'Chinese Yuan onshore', 
    'COP': 'Colombian Peso', 
    'CZK': 'Czech Koruna', 
    'DKK': 'Danish Krone', 
    'EGP': 'Egyptian Pound', 
    'EUR': 'Euro', 
    'GBP': 'British Pound Sterling', 
    'GHS': 'Ghanaian Cedi', 
    'HKD': 'Hong Kong Dollar', 
    'HRK': 'Croatian Kuna', 
    'HUF': 'Hungarian Forint', 
    'IDR': 'Indonesian Rupiah', 
    'ILS': 'Israeli New Sheqel', 
    'INR': 'Indian Rupee', 
    'ISK': 'Icelandic Krona', 
    'JOD': 'Jordanian Dinar', 
    'JPY': 'Japanese Yen', 
    'KES': 'Kenyan Shillings', 
    'KRW': 'South Korean Won', 
    'KWD': 'Kuwaiti Dinar', 
    'KZT': 'Kazakhstani Tenge', 
    'LBP': 'Lebanese Pound', 
    'LKR': 'Sri Lankan Rupee', 
    'MAD': 'Moroccan Dirham', 
    'MUR': 'Mauritian Rupee', 
    'MXN': 'Mexican Peso', 
    'MYR': 'Malaysian Ringgit', 
    'NGN': 'Nigerean Naira', 
    'NOK': 'Norwegian Krone', 
    'NZD': 'New Zealand Dollar', 
    'OMR': 'Omani Rial', 
    'PEN': 'Peruvian Nuevo Sol', 
    'PHP': 'Philippine Peso', 
    'PKR': 'Pakistani Rupee', 
    'PLN': 'Polish Zloty', 
    'QAR': 'Qatari Rial', 
    'RON': 'Romanian Leu', 
    'RUB': 'Russian Ruble', 
    'SAR': 'Saudi Arabian Riyal', 
    'SEK': 'Swedish Krona', 
    'SGD': 'Singapore Dollar', 
    'THB': 'Thai Baht', 
    'TND': 'Tunisian Dinar', 
    'TRY': 'Turkish Lira', 
    'TWD': 'Taiwanese Dollar', 
    'TZS': 'Tanzanian Shilling', 
    'UAH': 'Ukrainian Hryvnia', 
    'UGX': 'Ugandan Shilling', 
    'USD': 'US Dollar', 
    'VND': 'Vietnamese Dong', 
    'XAF': 'Central African Francs', 
    'XAG': 'Silver (troy ounce)', 
    'XAU': 'Gold (troy ounce)', 
    'XOF': 'West African CFA franc', 
    'XPD': 'Palladium', 
    'XPT': 'Platinum', 
    'ZAR': 'South African Rand', 
    'ZWL': 'Zimbabwean Dollar',
    'ADA': 'Cardano', 
    'ATOM': 'Atom', 
    'AVAX': 'Avalanche', 
    'AXS': 'Axis infinity', 
    'BCH': 'Bitcoin Cash', 
    'BNB': 'Binance Coin', 
    'BTC': 'Bitcoin', 
    'BTG': 'Bitcoin Gold', 
    'BUSD': 'Binance USD', 
    'DAI': 'DAI', 
    'DASH': 'Dashcoin', 
    'DOGE': 'DogeCoin', 
    'DOT': 'Polkadot', 
    'EGLD': 'Elrond Egold', 
    'ENJ': 'ENJ', 
    'EOS': 'EOS Platform', 
    'ETC': 'Ethereum Classic', 
    'ETH': 'Ethereum', 
    'FIL': 'Filecoin', 
    'FLOW': 'Flow', 
    'FTM': 'Fantom USD', 
    'FTT': 'FTX Token', 
    'GALA': 'Gala', 
    'HBAR': 'Hbar', 
    'HNT': 'Helium', 
    'ICP': 'Internet Computer Price ', 
    'LINK': 'Chainlink', 
    'LRC': 'Loopring', 
    'LTC': 'Litecoin', 
    'LUNA': 'Luna', 
    'MANA': 'Decentraland', 
    'MATIC': 'Matic', 
    'NEAR': 'Near', 
    'NEO': 'NEO', 
    'ROSE': 'Rose', 
    'SAND': 'Sandbox', 
    'SHIB': 'Shiba inu', 
    'SOL': 'Solana', 
    'THETA': 'Theta', 
    'TRX': 'Tron', 
    'UNI': 'Uniswap', 
    'USDT': 'Tether', 
    'UST': 'Terra USD', 
    'VET': 'Vechain', 
    'XLM': 'Stellar', 
    'XMR': 'Monero', 
    'XRP': 'Ripple', 
    'XTZ': 'Tezos'
    }

#Slectbox list
currencies = list(pair.keys())

#Function of Convert button
def convert():
    """Display Conversion Result"""
    try:
        from_currency = from_currency_var.get()[:to_currency_var.get().find(" ")]
        to_currency = to_currency_var.get()[:to_currency_var.get().find(" ")]
        amount = float(amount_entry.get())
        if from_currency == to_currency:
            result = amount
            rate = "1"  # No conversion rate if same currency
        else:
            rate , result = convert_currency(amount, from_currency, to_currency)
        conversion_result_label.config(text="Conversion Result",font=("Helvetica", 12))
        result_label.config(text=f"Converted Amount: {result} {to_currency}")
        rate_label.config(text=f"Conversion Rate: {rate} {from_currency} to {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Setting up the main window
window = tk.Tk()
window.title("Pycurrency Hub Currency Converter")
window.geometry("500x400")

# Header
header_label = tk.Label(window, text="Currency Converter")
header_label.pack(pady=10)

# Currency selection
from_currency_var = tk.StringVar(value="")
to_currency_var = tk.StringVar(value="")

# Widgets
amount_label = tk.Label(window, text="Amount:")
amount_label.pack(pady=5)

amount_entry = tk.Entry(window)
amount_entry.pack(pady=5)

# From Currency
from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.pack(pady=5)

from_currency_combobox = ttk.Combobox(window, textvariable=from_currency_var, values=currencies)
from_currency_combobox.pack(pady=5)

# To Currency
to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.pack(pady=5)

to_currency_combobox = ttk.Combobox(window, textvariable=to_currency_var, values=currencies)
to_currency_combobox.pack(pady=5)

# Button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result
conversion_result_label = tk.Label(window, text="")
conversion_result_label.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

rate_label = tk.Label(window, text="")
rate_label.pack(pady=5)

# Run the application
window.mainloop()
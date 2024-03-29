exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.15,
    "INR": 74.35,  # Add INR to the exchange rates
    # Add more currencies and exchange rates here
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency"
    
    converted_amount = amount / exchange_rates[from_currency] * exchange_rates[to_currency]
    return converted_amount

# Example usage
amount = 100
from_currency = "USD"
to_currency = "INR"  # Change to INR
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "conversion_rates" in data:
            exchange_rate = data["conversion_rates"].get(target_currency)
            if exchange_rate:
                return exchange_rate
        raise KeyError("Invalid currency or conversion rate not found.")
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"An error occurred: {e}")
        return None

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount
    return None

amount = 100
base_currency = "USD"
target_currency = "EUR"

converted_amount = convert_currency(amount, base_currency, target_currency)
if converted_amount:
    print(f"{amount} {base_currency} is equivalent to {converted_amount} {target_currency}")
else:
    print("Currency conversion failed.")
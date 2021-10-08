from binance import Client
from app.core.config import settings
from fastapi import APIRouter

client = Client(settings.API_KEY, settings.API_SECRET)

router = APIRouter()


@router.get("/get-coin")
def get_coin_price():
    result = get_coin_price_binance()
    return result


def get_coin_price_binance():
    most_percent_change_list = []
    tickers = client.get_ticker()
    for i in tickers:
        if float(i["priceChangePercent"]) >= 50.0:
            most_percent_change_list.append(i)
    return most_percent_change_list

    # if i['symbol'] == 'CAKEUSDT':
    #     print(float(i["priceChangePercent"]))
    #     return i
    #     print(i)


# print(tickers)


# from forex_python.converter import CurrencyRates

# c = CurrencyRates()

# print(c.get_rate('USD', 'THB'))

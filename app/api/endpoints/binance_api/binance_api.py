from binance import Client
from app.core.config import settings
from fastapi import APIRouter

client = Client(settings.API_KEY, settings.API_SECRET)

router = APIRouter()


@router.get("/get-coin")
def get_coin_price(is_high: bool, percent_change: int):
    tickers = connect_binance_api()
    result = get_coin_price_binance(tickers, is_high, percent_change)
    return result


def connect_binance_api():
    tickers = client.get_ticker()
    return tickers


def get_coin_price_binance(tickers, is_high, percent_change):
    most_percent_change_list = []
    if is_high:
        for i in tickers:
            if float(i["priceChangePercent"]) >= percent_change:
                most_percent_change_list.append(i)
    else:
        print(-percent_change)
        for i in tickers:
            if float(i["priceChangePercent"]) <= -percent_change:
                most_percent_change_list.append(i)
    return most_percent_change_list


@router.get("/get-specific-coin")
def get_specific_coin(coin_name: str):
    tickers = connect_binance_api()
    result = get_specific_coin_price_binance(tickers, coin_name)
    return result


def get_specific_coin_price_binance(tickers, coin_name):
    coin_list = []
    for i in tickers:
        if coin_name.upper() in i["symbol"]:
            coin_list.append(i)
    return coin_list

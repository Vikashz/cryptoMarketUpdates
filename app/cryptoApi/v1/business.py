import requests


def check_for_market_updates():
    """
    calls API: https://api.bittrex.com/v3/markets for fetching the market updates
    :return: Json
    """
    headers = {'Content-Type': 'application/json'}
    url = "https://api.bittrex.com/v3/markets"
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json()
    return False


def check_for_market_summary():
    """
    calls API: https://api.bittrex.com/v3/markets/summaries for fetching the market summary
    :return: json
    """
    url = "https://api.bittrex.com/v3/markets"
    headers = {'Content-Type': 'application/json'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json()
    return False


def check_for_market_summary_coin_wise(market_symbol):
    """
    calls API: https://api.bittrex.com/v3/markets/<marketSymbol>/summary for fetching the market summary
    :param market_symbol:
    :return: json
    """
    if market_symbol:
        url = f"https://api.bittrex.com/v3/markets/{market_symbol}/summary"
        headers = {'Content-Type': 'application/json'}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json()
    return False

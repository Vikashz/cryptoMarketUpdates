from app.cryptoApi.v1 import business as b


def test_check_for_market_updates():
    """
    test for checking check_for_market_summary method returns expect results
    after calling the API: https://api.bittrex.com/v3/markets for fetching the market updates
    """
    res = b.check_for_market_updates()
    assert isinstance(res, list) == True


def test_check_for_market_summary():
    """
    test for checking check_for_market_summary method returns expect results after calling the
    API: https://api.bittrex.com/v3/markets/summaries for fetching the market summary
    """
    res = b.check_for_market_summary()
    assert isinstance(res, list) == True


def test_check_for_market_summary_coin_wise():
    """
    Test for calling calls API: https://api.bittrex.com/v3/markets/<marketSymbol>/summary for fetching the market
    summary with correct data.
    """
    res = b.check_for_market_summary_coin_wise("eth-btc")
    assert isinstance(res, dict) == True


def test_check_for_market_summary_coin_wise_with_incorrect_request():
    """
    Test for calling calls API: https://api.bittrex.com/v3/markets/<marketSymbol>/summary for fetching the market
    summary with incorrect data
    """
    res = b.check_for_market_summary_coin_wise("xyz-btc")
    assert isinstance(res, dict) == False


def test_health():
    res = b.health()
    assert res["/market/<market_symbol>/summary"]["https://api.bittrex.com/v3/markets/<marketSymbol>/summary"] == "OK"
    assert res["/market/<market_symbol>/summary"]["Version"] == "V1"
    assert res["/market/summary"]["https://api.bittrex.com/v3/markets/summaries"] == "OK"
    assert res["/market/summary"]["Version"] == "V1"
    assert res["/market/updates"]["https://api.bittrex.com/v3/markets"] == "OK"
    assert res["/market/updates"]["Version"] == "V1"

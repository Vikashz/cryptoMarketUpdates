from app import app, jwt_required
from flask import jsonify
from app.cryptoApi.v1 import business as b


@app.route("/market/updates", methods=["GET"])
@jwt_required()
def crypto_market_updates():
    """
    calls API: https://api.bittrex.com/v3/markets for fetching the market updates
    :return: json data
    """
    try:
        resp = b.check_for_market_updates()
        if resp:
            response = {"status": True, "data": resp}
        else:
            response = {"status": False, "message": "Unable to fetch market updates"}
        return jsonify(response), 200
    except Exception as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/market/summary", methods=["GET"])
@jwt_required()
def crypto_market_summary():
    """
    calls API: https://api.bittrex.com/v3/markets/summaries for fetching the market summary
    :return: json
    """
    try:
        resp = b.check_for_market_summary()
        if resp:
            response = {"status": True, "data": resp}
        else:
            response = {"status": False, "message": "Unable to fetch market summary"}
        return jsonify(response), 200
    except Exception as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/market/<market_symbol>/summary", methods=["GET"])
@jwt_required()
def crypto_market_summary_coin_wise(market_symbol):
    """
    calls API: https://api.bittrex.com/v3/markets/<marketSymbol>/summary for fetching the market summary
    :return: json
    """
    try:
        resp = b.check_for_market_summary_coin_wise(market_symbol)
        if resp:
            response = {"status": True, "data": resp}
        else:
            response = {"status": False, "message": f"Unable to fetch market summery for {market_symbol.upper()}"}
        return jsonify(response), 200
    except Exception as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/health")
def health_status():
    try:
        response = b.health()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": False, "message": "API error: " + str(e)}), 500

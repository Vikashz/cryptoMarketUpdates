import requests, json
from flask import request, jsonify
from bson import json_util
from app import app, jwt_required
import app.authenticateUser.v1.business as b
from app.exceptions import ApiUserNotFound


@app.route("/signup", methods=["POST"])
def signup():
    """
    Creates new user
    :return:
    """
    try:
        json_data = json_util.loads(request.data)
        user_created = b.signup(json_data)
        if user_created:
            resp = {"status": True, "message": f"User created with id: {user_created}"}
        else:
            resp = {"status": False, "message": "Unable to created please check the payload"}
        return jsonify(resp), 200
    except Exception as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/login/<email>")
def login(email):
    try:
        password = request.args.get('password')
        valid_user = b.login(email, password)
        if valid_user:
            resp = {"status": True, "token": valid_user, "message": "Valid User"}
        else:
            resp = {"status": False, "message": "User not found, Make sure that the credentials used are correct"}
        return jsonify(resp), 200
    except ApiUserNotFound as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/")
@jwt_required()
def hello():
    url = "https://www.google.com"
    res = requests.get(url)
    return json.dumps(res.text)

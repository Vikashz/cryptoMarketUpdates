import json
import requests
from bson import json_util
from flask import request, jsonify

import app.authenticateUser.v1.business as b
from app import app, jwt_required
from app.exceptions import ApiUserNotFound


@app.route("/signup", methods=["POST"])
def signup():
    """
    Creates new user
    :return: status as true in case of success else false
    """
    try:
        json_data = json_util.loads(request.data)
        user_created = b.signup(json_data)
        status_code = 200
        if user_created:
            resp = {"status": True, "message": f"User created with id: {user_created}"}
        else:
            resp = {"status": False, "message": "Unable to created please check the payload"}
            status_code = 401
        return jsonify(resp), status_code
    except Exception as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


@app.route("/login/<email>")
def login(email):
    """
    Accepts email and password and validates the user.
    :param email: "xyz@gmail.com"
    :return: token
    """
    try:
        password = request.args.get('password')
        valid_user = b.login(email, password)
        status_code = 200
        if valid_user:
            resp = {"status": True, "token": valid_user, "message": "Valid User"}
        else:
            resp = {"status": False, "message": "User not found, Make sure that the credentials used are correct"}
            status_code = 401
        return jsonify(resp), status_code
    except ApiUserNotFound as e:
        response = {"status": False, "message": "API error: " + str(e)}
    return jsonify(response), 500


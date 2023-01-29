from app import create_access_token, mongo
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app.exceptions import ApiUserException


def signup(json_data):
    user_emai = json_data.get("email", "")
    password = json_data.get("password", "")
    user_exists = mongo.api_user.find_one({"email": user_emai})
    if user_exists:
        raise ApiUserException("User alredy in our system")
    if user_emai and password:
        create_api_user = {
            "first_name": json_data.get('first_name', ''),
            "last_name": json_data.get('last_name', ''),
            "email": user_emai,
            "password": generate_password_hash(password)
        }
        new_user_created = mongo.api_user.insert_one(create_api_user)
        return new_user_created.inserted_id
    return False


def login(email, password):
    user_exists = mongo.api_user.find_one({"email": email})
    if user_exists:
        if check_password_hash(user_exists["password"], password):
            return issue_access_token_for_api_user(email)
    else:
        return False


def issue_access_token_for_api_user(api_user):
    return create_access_token(identity=api_user, expires_delta=datetime.timedelta(hours=24))

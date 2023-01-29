from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from app.constants import mongo_uri, db_name, secret_key as sk
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = mongo_uri
app.config["JWT_SECRET_KEY"] = sk
jwt = JWTManager(app)
mongo = MongoClient(mongo_uri)
mongo = mongo[db_name]


from app.authenticateUser.v1 import views


if __name__ == '__main__':
    app.run(debug=True)


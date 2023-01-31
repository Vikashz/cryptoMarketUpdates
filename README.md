# cryptoMarketUpdates
APIs for fetching the cryptocurrency market price

**Requirements:**
1) python 3
2) mongodb for storing credentials
3) postman

**Steps for setting up the project:**
1) install requirements.txt
2) start the mongodb using command **sudo systemctl start mongod** create a mongo db and name it as cryptogeek
3) start flask app using command **flask run**
4) call the post API for creating a user http://127.0.0.1:5000/signup with below json payload {"email":"vk@mailinator.com",
"password":"lol123",
"first_name": "Vikash",
"last_name": "Kumar"} 
5) Now call the GET API http://127.0.0.1:5000/login/vk@mailinator.com?password=lol123 for fetching the access token
6) If you are using postman then put the token in Bearer Token and then you can call the below APIs:
7) http://127.0.0.1:5000/market/updates
8) http://127.0.0.1:5000//market/summary
9) http://127.0.0.1:5000/market/xyz-btc/summary



**Additional items:**
1) Unit tests with overall **72 %** coverage.
Command for running the coverage: **coverage run -m pytest --disable-warnings app/tests** then **coverage html**
2) Dockerfile for creating app image
Command for running dockerfile **docker image build -t crypto_flask .** and for running the image **docker run -p 5000:5000 -d crypto_flask**

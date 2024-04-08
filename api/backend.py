from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/api/books")
def home():
    user = {
        "user_id" : 123,
        "name": "YOUSSEF",
        "Email": "Yousef@gmail.com"
    }
    return jsonify(user), 200 




if __name__ == "__main__":
    app.run(host='127.0.0.2', debug=True)

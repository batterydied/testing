from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({'message': 'this is root'})

@app.route("/about")
def about():
    return jsonify({'message': 'this is the about page'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask app running on EKS 2285!"

@app.route('/api/user')
def user():
    return jsonify({"id": 1, "name": "Alice"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


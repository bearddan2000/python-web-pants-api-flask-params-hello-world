from flask import Flask, jsonify
app = Flask(__name__)

greeting = {"message": "hello world"}

@app.route('/')
def hello():
    return jsonify(greeting)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)

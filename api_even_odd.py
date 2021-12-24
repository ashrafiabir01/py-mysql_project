from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def index():
    return "<p>Hi</p>"
@app.route("/number/<int:a>")
def hello_world(a):

    if a % 2 == 0:
        result = {
            "number" : a,
            "result":"This is even number",
            "host":"localhost"
        }
        return jsonify(result)
    else:
        result = {
            "number": a,
            "result": "This is odd number",
            "host": "localhost"
        }
        return jsonify(result)
@app.route("/api/<int:k>")
def shoe_parameter(k):
    res = jsonify(k)
    return res
if __name__ == "__main__":
    print("add")
    app.run(host="127.0.0.1", port=3333, debug=True)

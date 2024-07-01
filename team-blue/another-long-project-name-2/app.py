from flask import Flask
import os

app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return "healthy"

@app.route("/readyz")
def readyz():
    greeting = "Hello, World!"
    print(greeting)
    return "ok"

@app.route("/")
def hello():
    return "This is project2, it does another thing!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False,host='0.0.0.0',port=port)

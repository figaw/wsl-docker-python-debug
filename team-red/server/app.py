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
    f = open("/mnt/version", "r")
    content = f.read().replace("\n", "")
    return f'This is team-red server, version {content}!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False,host='0.0.0.0',port=port)

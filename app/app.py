from flask import Flask
import os

app = Flask(__name__)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.route("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "dev")}, 200


@app.route("/crash")
def crash():
    os._exit(1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

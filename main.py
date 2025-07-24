from flask import Flask, redirect, abort
from bridge import *

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return redirect("https://github.com/MathiasDPX/scrapbook.md")


@app.route("/post/<postid>", methods=["GET"])
def get_post(postid:str):
    return abort(501)


@app.route("/latest-post/<username>", methods=["GET"])
def get_latest_post(username:str):
    user = ScrapbookUser.from_username(username)
    if type(user) == int:
        return abort(user)

    return abort(501)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

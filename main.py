from flask import Flask, redirect, abort, send_file, request
from io import BytesIO
from bridge import *
from image import *
import time

app = Flask(__name__)

def serve_image(img):
    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route("/", methods=["GET"])
def index():
    return redirect("https://github.com/MathiasDPX/scrapbook.md")


@app.route("/latest-post/<username>", methods=["GET"])
def get_latest_post(username:str):
    version = request.args.get("v", default=time.time(), type=int)

    user = ScrapbookUser.from_username(username)
    if type(user) == int:
        return abort(user)

    latest = None
    for post in user.posts:
        if post.timestamp <= version:
            latest = post
            break

    if len(user.posts) == 0 or latest == None:
        img = get_empty()
    else:
        img = draw_card(
            text=latest.text,
            author="@"+username
        )
    
    return serve_image(img)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return redirect("https://github.com/MathiasDPX/scrapbook.md")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

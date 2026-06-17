from flask import Flask, render_template, request, jsonify
from core.brain import brain
from training.txt_trainer import train_txt

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data["message"]
    mode = data["mode"]

    result = brain(message, {
        "mode": mode
    })

    return jsonify(result)


@app.route("/train", methods=["POST"])
def train():
    count = train_txt()
    return {"status": "trained", "chunks": count}


if __name__ == "__main__":
    app.run(debug=True)
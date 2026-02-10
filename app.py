from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_input = request.form["msg"]
        reply = get_response(user_input)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)

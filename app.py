from flask import Flask, render_template, request, flash

# initialize app
app = Flask(__name__)

# renders the default page
@app.route("/")
def index():
    return render_template("index.html")

# renders the default page
@app.route("/live")
def live():
    return render_template("live.html")
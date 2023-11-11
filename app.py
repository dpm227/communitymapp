from flask import Flask, render_template, request, flash

# initialize app
app = Flask(__name__)

app.secret_key = 'secret_key'

# renders the default page
@app.route("/")
def index():
    return render_template("index.html")
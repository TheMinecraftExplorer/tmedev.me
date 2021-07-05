from flask import Flask, render_template

app = Flask("Website")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
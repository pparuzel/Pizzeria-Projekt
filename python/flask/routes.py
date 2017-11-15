from flask import redirect, render_template, url_for

from python.flask.app import app

@app.route('/')
def index():
    return render_template('index.html')

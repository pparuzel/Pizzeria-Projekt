from flask import Flask  # external
from flask_flatpages import FlatPages  # external
from flask_frozen import Freezer  # external

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

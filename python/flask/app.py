from flask import Flask

app = Flask(__name__)
app.static_folder = '../../html/static'
app.template_folder = '../../html/templates'
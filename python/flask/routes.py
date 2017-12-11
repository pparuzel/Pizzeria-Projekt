from flask import redirect, render_template, url_for, request

from python.flask.app import app


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        print('† index')
        return render_template('index.html')


@app.route('/profile', methods=['GET'])
def user_profile():
    if request.method == 'GET':
        return render_template('profile.html')


@app.route('/menu', methods=['GET'])
def show_menu():
    if request.method == 'GET':
        return render_template('menu.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print('login')
        return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print('register')
        return redirect(url_for('index'))


@app.route('/update_user', methods=['POST'])
def update_user():
    if request.method == 'POST':
        print('user update')
        return redirect(url_for('user_profile'))

from flask import redirect, render_template, url_for, request

from python.flask.app import app

#
# guest
#

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        print('† index')
        is_logged_in = True
        return render_template('index.html', logged_in=is_logged_in)


# get user's info from database
@app.route('/profile', methods=['GET'])
def user_profile():
    if request.method == 'GET':
        return render_template('profile.html')


# validate user's info from database
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print('login')
        return redirect(url_for('index'))


# add user to database
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print('register')
        return redirect(url_for('index'))


#
# menu
#

@app.route('/menu', methods=['GET'])
def show_menu():
    # read from DB
    pizzas = [
        ['margarita', 'sos, ser, oregano, bazylia', 21.50],
        ['salami', 'sos, ser, oregano, salami', 22.50],
        ['z szynką', 'sos, ser, oregano, szynka', 22.50],
        ['hawajska', 'sos, ser, oregano, ananas, szynka', 24.50]
    ]
    if request.method == 'GET':
        is_logged_in = True
        return render_template('menu.html', products=pizzas, logged_in=is_logged_in)


@app.route('/show_order', methods=['POST', 'GET'])
def show_current_order():
    import random
    if request.method == 'POST':
        selected_products = request.form.getlist('check_group')
        if len(selected_products) > 0:
            print(selected_products)
            delivery_time = random.randint(45,90)
            return render_template('order_page.html',
                                   selected_products=selected_products,
                                   delivery_time=delivery_time)
        else:
            return redirect(url_for('show_menu'))
    elif request.method == 'GET':
        return render_template('order_page.html')


@app.route('/make_order', methods=['POST', 'GET'])
def make_order():
    # put order into DB
    # show pop up
    return redirect(url_for('index'))


#
# user
#

# update user with database
@app.route('/update_user', methods=['POST'])
def update_user():
    if request.method == 'POST':
        print('user update')
        return redirect(url_for('user_profile'))





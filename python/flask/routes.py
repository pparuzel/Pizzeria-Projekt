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
        return render_template('client/index.html', logged_in=is_logged_in)


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
# order
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
        return render_template('client/menu.html', products=pizzas, logged_in=is_logged_in)


@app.route('/show_order', methods=['POST', 'GET'])
def show_current_order():
    import random
    if request.method == 'POST':
        selected_products = request.form.getlist('check_group')
        if len(selected_products) > 0:
            print(selected_products)
            delivery_time = random.randint(45, 90)
            address = ['Alejkowa', '45b/4', 'Kraków']
            return render_template('client/order_page.html',
                                   selected_products=selected_products,
                                   delivery_time=delivery_time,
                                   address=address)
        else:
            return redirect(url_for('show_menu'))
    elif request.method == 'GET':
        return render_template('client/order_page.html')


@app.route('/change_order_address', methods=['POST', 'GET'])
def change_address():
    if request.method == 'POST':
        return redirect(url_for('show_current_order'))


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


# get user's info from database
@app.route('/profile', methods=['GET'])
def user_profile():
    if request.method == 'GET':
        user_info = {
            'first_name': 'Piotr',
            'last_name': 'Persona',
            'email': 'persona.piotr@gmail.com',
            'phone': '123456789'
        }
        return render_template('client/profile.html',
                               username=user_info['first_name'],
                               user_info=user_info.values())


@app.route('/verify_password', methods=['POST', 'GET'])
def verify_password():
    if request.method == 'POST':
        # handle validation
        return redirect(url_for('user_profile'))


#
# admin
#

@app.route('/admin_login')
def admin_login_page():
    return render_template('admin/login.html')


@app.route('/admin_index', methods=['POST', 'GET'])
def admin_index_page():
    return render_template('admin/index.html')


# TODO password check
@app.route('/admin', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'GET':
        return redirect(url_for('admin_login_page'))
    if request.method == 'POST':
        return redirect(url_for('admin_index_page'))


@app.route('/add_product_page', methods=['POST', 'GET'])
def add_product_page():
    if request.method == 'GET':
        return render_template('admin/add_product.html')


@app.route('/show_products', methods=['POST', 'GET'])
def show_products():
    return render_template('admin/products.html')


@app.route('/add_product/<product_type>', methods=['POST', 'GET'])
def add_product(product_type):
    if request.method == 'POST':
        print(product_type)
        return redirect(url_for('add_product_page'))

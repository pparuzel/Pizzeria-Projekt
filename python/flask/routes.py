from flask import redirect, render_template, url_for, request

from python.flask.app import app
from python.flask.app import db
from python.flask.app import Topping, Order, Drink, User, Pizza
from python.flask.app import order_drink_relationship, order_pizza_relationship
from flask_admin import Admin as FlaskAdmin
from flask_admin.contrib.sqla import ModelView
from flask import session as session_handler
from copy import deepcopy


shopping_cart = {}

#
# guest
#


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        print('† index')
        email_in_session = 'email' in session_handler
        return render_template('client/index.html', logged_in=email_in_session)


# validate user's info from database
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if password == user.password:
            session_handler['email'] = (email, user.id)
            shopping_cart[email] = []
        return redirect(url_for('index'))


@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        if 'email' in session_handler:
            session_handler.pop('email')
        return redirect(url_for('index'))


# add user to database
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        password1 = request.form['password']
        password2 = request.form['password2']
        if password1 == password2:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            street = request.form['street']
            flat_nr = request.form['flat_nr']

            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1,
                street=street,
                flat_nr=flat_nr
            )

            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('index'))


#
# order
#

@app.route('/menu', methods=['GET'])
def show_menu():
    pizzas = Pizza.query.all()
    toppings = Topping.query.all()
    drinks = Drink.query.all()
    if request.method == 'GET':
        is_logged_in = 'email' in session_handler
        return render_template('client/menu.html',
                               logged_in=is_logged_in,
                               pizzas=pizzas,
                               toppings=toppings,
                               drinks=drinks
                               )


@app.route('/show_order', methods=['POST', 'GET'])
def show_current_order():
    import random
    if request.method == 'POST':
        selected_pizzas = request.form.getlist('check_group_pizza')
        amount_of_selected_pizzas = request.form['quantity']
        selected_toppings = request.form.getlist('check_group_topping')
        selected_drinks = request.form.getlist('check_group_drink')
        if len(selected_pizzas) > 0:
            print(selected_pizzas)
            print(selected_toppings)
            print(selected_drinks)
            print(amount_of_selected_pizzas)
            delivery_time = random.randint(45, 90)
            # get user's address
            address = ['Alejkowa', '45b/4', 'Kraków']
            return render_template('client/order_page.html',
                                   selected_pizzas=selected_pizzas,
                                   selected_toppings=selected_toppings,
                                   delivery_time=delivery_time,
                                   address=address)
        else:
            return redirect(url_for('show_menu'))
    elif request.method == 'GET':
        return render_template('client/order_page.html')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        selected_pizza = list(request.form)[0]
        amount_of_pizza = request.form[selected_pizza]
        pizza_size = request.form['select_size']
        selected_toppings = request.form.getlist('check_group_topping')
        toppings = [int(topping_id) for topping_id in selected_toppings]

        cart_pos = {
            'pizza': {
                'pizza_id': selected_pizza,
                'pizza_size': pizza_size,
                'amount': amount_of_pizza,
                'toppings': toppings
            }
        }

        user_email = session_handler['email'][0]
        shopping_cart[user_email].append(cart_pos)

        return redirect(url_for('show_menu'))


@app.route('/add_drink_to_cart', methods=['POST'])
def add_drink_to_cart():
    if request.method == 'POST':
        selected_drink = request.form['drink']

        drink_cart_pos = {
            'drink': selected_drink
        }

        user_email = session_handler['email'][0]
        shopping_cart[user_email].append(drink_cart_pos)
        return redirect(url_for('show_menu'))


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    if request.method == 'POST':
        to_remove = request.form['pos']
        user_email = session_handler['email'][0]
        shopping_cart[user_email].pop(int(to_remove))
    return redirect(url_for('show_cart'))


@app.route('/cart', methods=['GET'])
def show_cart():
    if request.method == 'GET':
        user_email = session_handler['email'][0]
        user_shopping_cart = shopping_cart[user_email]
        return render_template('client/cart.html', cart=user_shopping_cart)


@app.route('/change_order_address', methods=['POST', 'GET'])
def change_address():
    if request.method == 'POST':
        return redirect(url_for('show_current_order'))


@app.route('/make_order', methods=['POST', 'GET'])
def make_order():
    if request.method == 'POST':
        from datetime import datetime
        # put order into DB
        user_email = session_handler['email'][0]
        user_id = session_handler['email'][1]
        user = User.query.get(user_id)
        order = Order(date=datetime.now(), user=user, status='waiting')
        db.session.add(order)
        db.session.commit()
        cart = shopping_cart[user_email]
        for product in cart:
            for product_name, product_content in product.items():
                if product_name == 'pizza':
                    pizza_id = int(product_content['pizza_id'])
                    selected_pizza = Pizza.query.get(pizza_id)

                    insert_pizza_info = order_pizza_relationship.insert().values(
                        order=order.id,
                        pizza=selected_pizza.id,
                        size=product_content['pizza_size'],
                        amount=int(product_content['amount'])
                    )
                    db.engine.execute(insert_pizza_info)
                    db.session.commit()
                if product_name == 'drink':
                    drink_id = int(product_content)
                    selected_drink = Drink.query.get(drink_id)
                    order.drinks.append(selected_drink)
                    db.session.commit()

        print(order.pizzas)
        shopping_cart.pop(user_email)
        return redirect(url_for('index'))


#
# user
#

# update user with database
@app.route('/update_user', methods=['POST'])
def update_user():
    if request.method == 'POST':
        if 'email' in session_handler:
            user = User.query.get(session_handler['email'][1])

            first_name = request.form['first_name']
            last_name = request.form['last_name']
            street = request.form['street']
            flat_nr = request.form['flat_nr']

            if len(first_name) > 0:
                user.first_name = first_name
            if len(last_name) > 0:
                user.last = last_name
            if len(street) > 0:
                user.street = street
            if len(flat_nr) > 0:
                user.flat_nr = flat_nr

            db.session.commit()
            return redirect(url_for('user_profile'))
        else:
            return redirect(url_for('index')), 403


# get user's info from database
@app.route('/profile', methods=['GET'])
def user_profile():
    if request.method == 'GET':
        if 'email' in session_handler:
            user = User.query.get(session_handler['email'][1])
            user_info = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'street': user.street,
                'flat_nr': user.flat_nr
            }

            return render_template('client/profile.html',
                                   username=user_info['first_name'],
                                   user_info=user_info.values())
        else:
            return redirect(url_for('index')), 403


@app.route('/change_password', methods=['POST'])
def change_password():
    if request.method == 'POST':
        if 'email' in session_handler:
            user = User.query.get(session_handler['email'][1])
            user_password = user.password
            old_password = request.form['old_password']
            if user_password == old_password:
                new_password = request.form['new_password']
                repeat_new_password = request.form['repeat_new_password']
                if new_password == repeat_new_password:
                    user.password = new_password
                    db.session.commit()
                    return redirect(url_for('user_profile'))
            return "passwords does not match"
        else:
            return redirect(url_for('index'))


#
# admin
#

# views

class PizzaView(ModelView):

    can_create = True
    can_edit = True
    can_delete = True


class PizzaToppingsView(ModelView):

    can_create = True
    can_edit = True
    can_delete = True


class DrinkView(ModelView):

    can_create = True
    can_edit = True
    can_delete = True


class UserView(ModelView):

    can_create = False
    can_edit = False
    can_delete = False

    column_list = ('first_name', 'last_name', 'email', 'street', 'flat_nr')


class OrderView(ModelView):

    can_create = False
    can_edit = True
    can_delete = False

    column_list = ('date', 'status', 'user', 'pizzas', 'drinks', 'order_value')


def setup_admin_view():
    admin = FlaskAdmin(app, name='pizzeria-admin', template_mode='bootstrap3', url='/admin')

    pizza_view = PizzaView(Pizza, db.session)
    pizza_toppings_view = PizzaToppingsView(Topping, db.session)
    drink_view = DrinkView(Drink, db.session)
    user_view = UserView(User, db.session)
    order_view = OrderView(Order, db.session)

    admin.add_view(order_view)
    admin.add_view(pizza_view)
    admin.add_view(pizza_toppings_view)
    admin.add_view(drink_view)
    admin.add_view(user_view)

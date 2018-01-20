import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import select

app = Flask(__name__)
app.static_folder = '../../html/static'
app.template_folder = '../../html/templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/Pizzeria?charset=utf8'
app.config['SECRET_KEY'] = os.urandom(32)


db = SQLAlchemy(app)


order_pizza_relationship = db.Table(
    'order_pizza_relationship',
    db.Column('id', mysql.INTEGER(unsigned=True), primary_key=True, autoincrement=True, nullable=False),
    db.Column('order', db.Integer, db.ForeignKey('order.id'), nullable=False),
    db.Column('pizza', db.Integer, db.ForeignKey('pizza.id'), nullable=False),
    db.Column('size', db.Enum('small', 'medium', 'large'), nullable=False),
    db.Column('amount', db.Integer, nullable=False)
)

order_drink_relationship = db.Table(
    'order_drink_relationship',
    db.Column('order', db.Integer, db.ForeignKey('order.id')),
    db.Column('drink', db.Integer, db.ForeignKey('drink.id'))
)

# entities

class PizzeriaAdmin(db.Model):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(320), nullable=False)


class Pizza(db.Model):

    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    ingredients = db.Column(db.String(90), nullable=False)
    price_small = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)
    price_medium = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)
    price_large = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)
    valid = db.Column(mysql.BOOLEAN(create_constraint=True), default=True, nullable=False)

    def __repr__(self):
        return ', '.join([
            str(self.name),
            str(self.ingredients),
            str(self.price_small),
            str(self.price_medium),
            str(self.price_large)
        ])


class Topping(db.Model):

    __tablename__ = 'topping'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)

    def __repr__(self):
        return ' '.join([
            str(self.name),
            str(self.price)
        ])


class Drink(db.Model):

    __tablename__ = 'drink'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)

    def __repr__(self):
        return ', '.join([
            str(self.name),
            str(self.price)
        ])


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(320), nullable=False, unique=True)
    password = db.Column(db.String(320), nullable=False)
    street = db.Column(db.String(70), nullable=False)
    flat_nr = db.Column(db.String(12), nullable=False)

    orders = db.relationship(
        'Order',
        backref='user',
        lazy='dynamic'
    )

    def __repr__(self):
        return ', '.join([
            str(self.first_name),
            str(self.last_name),
            str(self.email)
        ])


class Order(db.Model):

    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(mysql.ENUM('waiting', 'paid', 'rejected'), nullable=False, default='waiting')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    pizzas = db.relationship(
        'Pizza',
        secondary='order_pizza_relationship',
    )

    drinks = db.relationship(
        'Drink',
        secondary=order_drink_relationship
    )

    @property
    def order_value(self):
        pizzas_value = 0
        target = order_pizza_relationship
        select_query = select([
            target
        ]).where(target.c.order == self.id)
        query_result = db.engine.execute(select_query)

        for data in query_result:
            pizza_id = data[2]
            pizza_size = data[3]
            amount = data[4]
            pizza = Pizza.query.get(pizza_id)
            if pizza_size == 'small':
                pizzas_value += amount * pizza.price_small
            elif pizza_size == 'medium':
                pizzas_value += amount * pizza.price_medium
            elif pizza_size == 'large':
                pizzas_value += amount * pizza.price_large

        drinks_value = sum(drink.price for drink in self.drinks)
        value = pizzas_value + drinks_value
        return value

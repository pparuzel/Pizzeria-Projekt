import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql

app = Flask(__name__)
app.static_folder = '../../html/static'
app.template_folder = '../../html/templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/Pizzeria?charset=utf8'
app.config['SECRET_KEY'] = os.urandom(32)


db = SQLAlchemy(app)


pizza_toppings_relationship = db.Table(
    'pizza_toppings_relationship',
    db.Column('pizza', db.Integer, db.ForeignKey('pizza.id')),
    db.Column('pizza_topping', db.Integer, db.ForeignKey('pizza_toppings.id'))
)


order_product_relationship = db.Table(
    'order_product_relationship',
    db.Column('order', db.Integer, db.ForeignKey('order.id')),
    db.Column('pizza', db.Integer, db.ForeignKey('pizza.id')),
    db.Column('drink', db.Integer, db.ForeignKey('drink.id')),
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


class PizzaToppings(db.Model):

    __tablename__ = 'pizza_toppings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(mysql.DECIMAL(precision=10, scale=2, unsigned=True), nullable=False)

    def __repr__(self):
        return ', '.join([
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

    pizzas = db.relationship(
        "Pizza",
        secondary=order_product_relationship
    )

    drinks = db.relationship(
        "Drink",
        secondary=order_product_relationship
    )


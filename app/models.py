# Imports

from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_stores = db.relationship("Store", backref="owner", lazy='dynamic')

    def __init__(self, fname, lname, email, username, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    # flask-login methods
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return ""


class Store(db.Model):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, nullable=False)
    store_description = db.Column(db.String, nullable=False)
    store_owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    store_product = db.relationship("Product", backref="storage", lazy='dynamic')

    def __init__(self, store_name, store_description, store_owner):
        self.store_name = store_name
        self.store_description = store_description
        self.store_owner = store_owner

    def __repr__(self):
        return ""


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    product_description = db.Column(db.String, nullable=False)
    store_home = db.Column(db.Integer, db.ForeignKey('store.id'))

    def __init__(self, product_name, product_description, store_home):
        self.product_name = product_name
        self.product_description = product_description
        self.store_home = store_home

    def __repr__(self):
        return ""

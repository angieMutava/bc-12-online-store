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
    store = relationship("Store", backref="owner")

    def __init__(self, fname, lname, email, username, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    # Use usermixin as an alternative the the below flask-login methods
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class Store(db.Model):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, nullable=False)
    store_description = db.Column(db.String, nullable=False)
    store_image = db.Column(db.String, nullable=False)
    store_owner = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, id, store_name, store_description, store_owner, store_image="na.jpg"):
        self.store_name = store_name
        self.store_description = store_description
        self.store_image = store_image
        self.store_owner = store_owner

    def __repr__(self):
        return '<{} {} {} {}>'.format(self.store_name, self.store_description, self.store_image, self.store_owner)

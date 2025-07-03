from flask_sqlalchemy import SQLAlchemy
from Controllers import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

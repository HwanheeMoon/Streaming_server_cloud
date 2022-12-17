from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Comments(db.Model):
    __tabllename__ = 'Comments'

    id = db.Column(db.Integer, primary_key=True)
    vdNum = db.Column(db.Integer)
    writer = db.Column(db.String(10))
    comment = db.Column(db.String(64))


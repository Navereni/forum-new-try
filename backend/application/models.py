from application import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    comments = db.relationship('Comments', backref='posts')

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
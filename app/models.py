from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(128))
    articles = db.relationship('Article', backref='author', lazy='dynamic')
    logs = db.relationship('Log', backref='logauthor', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1028))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Article {}'.format(self.body)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(64))
    difficulty = db.Column(db.String(5))
    body = db.Column(db.String(240))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'User: {}, Log: {}'.format(self.logauthor, self.body)
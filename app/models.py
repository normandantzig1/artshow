from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password_hash=db.Column(db.String(120), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    submissions =db.relationship('Submission', backref='Author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    ###NEW
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(80), index=True, unique=False, nullable=True)
    link = db.Column(db.String(150), index=True, unique=False, nullable=True)
    description = db.Column(db.Text, index=True, unique=False, nullable=True)
    title = db.Column(db.String(150), index=True, unique=False, nullable=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    ###BODY of text
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.relationship('Rating', backref='rated', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.title)
    
    
class Rating(db.Model):
    ##run AVG on rating in querry
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, index=True, nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
                        
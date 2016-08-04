from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(64))
    desc = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)

class TestCase(db.Model):
    __tablename__='test_cases'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    desc = db.Column(db.String(64))
    expect = db.Column(db.String(64))
    hasDetail= db.Column(db.Integer)
    parentCaseId = db.Column(db.Integer)
    productID = db.Column(db.Integer)
    version = db.Column(db.Integer)
    ctime = db.Column(db.DateTime,default=datetime.now)
    utime = db.Column(db.DateTime,onupdate=datetime.now)


class TestPlan(db.Model):
    __tablename__='test_plans'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    productID = db.Column(db.Integer)
    desc = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)


class TestStep(db.Model):
    __tablename__='test_steps'
    id = db.Column(db.Integer,primary_key=True)
    testCaseId = db.Column(db.Integer)
    desc = db.Column(db.String(64))
    expect = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)

class TestResult(db.Model):
    __tablename__='test_results'
    id = db.Column(db.Integer,primary_key=True)
    TestPlanid = db.Column(db.Integer)
    testCaseId = db.Column(db.Integer)
    testStepId = db.Column(db.Integer)
    result = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)


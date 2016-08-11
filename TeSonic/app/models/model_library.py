from . import *



#TODO: add test method for models
class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(64))
    desc = db.Column(db.String(64))

    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)


class Request(db.Model):
    __tablename__='test_request'
    id = db.Column(db.Integer,primary_key=True)
    TestPlanid = db.Column(db.Integer)
    testCaseId = db.Column(db.Integer)
    testStepId = db.Column(db.Integer)
    result = db.Column(db.Integer)
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


class TestPolicy(db.Model):
    __tablename__='test_policy'
    id = db.Column(db.Integer,primary_key=True)
    TestPlanid = db.Column(db.Integer)
    testCaseId = db.Column(db.Integer)
    testStepId = db.Column(db.Integer)
    result = db.Column(db.Integer)
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

    
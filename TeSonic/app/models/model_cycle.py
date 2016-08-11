from . import *





class TestPlan(db.Model):
    __tablename__='test_plans'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    productID = db.Column(db.Integer)
    desc = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, onupdate=datetime.now)

class TestCycle(db.Model):
    __tablename__='test_cycles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(64))
    productID = db.Column(db.Integer)
    desc = db.Column(db.String(64))
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
from . import *



#TODO: add test method for models
class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(64), nullable=False,unique=True)
    desc = db.Column(db.String(64))
    type = db.Column(db.Integer)

    owner = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    utime = db.Column(db.DateTime, onupdate=datetime.utcnow)

    @staticmethod
    def fake(n=10):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(n):
            p = Product(productName = forgery_py.forgery.personal.language(),
                        desc = forgery_py.basic.text(50,5))
            db.session.add(p)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()



class Request(db.Model):
    __tablename__='test_request'
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer)
    name = db.Column(db.String(64))
    desc = db.Column(db.String(64))
    priority = db.Column(db.Integer)
    owner = db.Column(db.Integer)
    status = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    utime = db.Column(db.DateTime, onupdate=datetime.utcnow)

    @staticmethod
    def fake(n=10):
        from sqlalchemy.exc import IntegrityError
        from random import seed,randint
        import forgery_py

        seed()
        product_count = Product.query.count()
        for i in range(n*product_count):
            product = Product.query.offset(randint(0, product_count - 1)).first()
            request = Request(product_id = product.id,
                        name = forgery_py.forgery.personal.language(),
                        desc = forgery_py.basic.text(50,5))
            db.session.add(request)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

class TeamMapper(db.Model):
    __tablename__="team_mapper"
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    ctime = db.Column(db.DateTime,default=datetime.utcnow)
    utime = db.Column(db.DateTime,onupdate=datetime.utcnow)


class TestStep(db.Model):
    __tablename__='test_steps'
    id = db.Column(db.Integer,primary_key=True)
    testCaseId = db.Column(db.Integer)
    desc = db.Column(db.String(64))
    expect = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    utime = db.Column(db.DateTime, onupdate=datetime.utcnow)


class TestPolicy(db.Model):
    __tablename__='test_policy'
    id = db.Column(db.Integer,primary_key=True)
    TestPlanid = db.Column(db.Integer)
    testCaseId = db.Column(db.Integer)
    testStepId = db.Column(db.Integer)
    result = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.utcnow)
    utime = db.Column(db.DateTime, onupdate=datetime.utcnow)



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
    ctime = db.Column(db.DateTime,default=datetime.utcnow)
    utime = db.Column(db.DateTime,onupdate=datetime.utcnow)


    
from flask import render_template, redirect, request, url_for, flash,jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask.ext.login import login_user, logout_user, login_required
from . import api
from ..models import User,Product,db
from .forms import LoginForm

#Initial resource with restful-api
api_Resource = Api(api)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@api.route('/tasks', methods=['GET'])
def test():
    return jsonify({'tasks': tasks})


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}



class ProductItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('product_Name', required=True, help='A Product Name is Required')
    def get(self,id):
        product = Product.query.filter_by(id = id).first()
        return product.productName

    def put(self,id):
        args = self.parser.parse_args()
        product = Product.query.filter_by(id=id).first()
        print product
        product.productName = args['product_Name']
        print product.productName
        db.session.add(product)
        db.session.commit()
        return product.productName


class ProductList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Name is Required')
    parser.add_argument('desc', required=True, help='desc is Required')
    parser.add_argument('type', required=True, help='type is Required')
    parser.add_argument('owner', required=True, help='owner is Required')
    def post(self):
        args = self.parser.parse_args()
        print args
        name = args['name']
        product = Product.query.filter_by(productName=name).first()
        if product == None:
            p = Product(productName = name,
                        desc = args['desc'],
                        type = args['type'],
                        #TODO: change this either
                        Owner = args['owner'])
            db.session.add(p)
            db.session.commit()
            return "success"
        else:
            return "Duplicated"



#Add resource

api_Resource.add_resource(TodoItem, '/todos/<int:id>')
api_Resource.add_resource(ProductItem, '/product/<int:id>')
api_Resource.add_resource(ProductList, '/products')
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


parser = reqparse.RequestParser()
parser.add_argument('product_Name',required=True,help='A Product Name is Required')
class Products(Resource):
    def get(self,id):
        product = Product.query.filter_by(id = id).first()
        return product.productName

    def put(self,id):
        args = parser.parse_args()
        product = Product.query.filter_by(id=id).first()
        print product
        product.productName = args['product_Name']
        print product.productName
        db.session.add(product)
        db.session.commit()
        return product.productName



#Add resource
api_Resource.add_resource(TodoItem, '/todos/<int:id>')
api_Resource.add_resource(Products, '/products/<int:id>')
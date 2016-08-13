from flask import render_template, redirect, request, url_for, flash,jsonify
from flask.ext.login import login_user, logout_user, login_required
from . import api
from ..models import User
from .forms import LoginForm

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
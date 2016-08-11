from flask import render_template
from . import main
from .. import auth
from flask.ext.login import login_user, logout_user, login_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

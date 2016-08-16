from flask import render_template
from . import main
from .. import auth
from flask.ext.login import login_user, logout_user, login_required

@main.route('/')
def index():
    from datetime import datetime

    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/dashboard')
#@login_required
def dashboard():
    return render_template('dashboard.html')

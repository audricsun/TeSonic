from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import api
from ..models import User
from .forms import LoginForm


@api.route('/get', methods=['GET'])
def test():
    return "empty"
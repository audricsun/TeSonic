from flask import Blueprint

cycles = Blueprint('cycles', __name__)

from . import views
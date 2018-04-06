from flask import Blueprint,render_template

main = Blueprint('main',__name__)

from . import views
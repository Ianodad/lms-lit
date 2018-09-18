from flask import Blueprint

# auth
auth = Blueprint('auth', __name__)

# auth views and forms import
from . import views, forms

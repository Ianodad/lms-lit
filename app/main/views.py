from flask import render_template, redirect, url_for, abort
# settings.py
import os
from config import APP_STATIC

# importing main from main blueprint
from . import main
# importing database
# from .. import db

# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm

# with open(os.path.join(APP_STATIC, 'content.txt')) as f:
#     content = f.read()

# with open('content.txt', 'r') as f:
#     data = f.readlines()


@main.route('/')
def index():
    new_content = data
    title = 'Home is best'

    return render_template('index.html', title=title, new_content=new_content)


@main.route('/courses')
def course():

    return render_template('content.html', title='title', content=content)

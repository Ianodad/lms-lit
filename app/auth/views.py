# from user we are import use model
from flask import render_template, redirect, url_for, flash, request
from ..models import Student
# importing database form SQLalchemy
from .. import db
# from flask import login user
from flask_login import login_user, logout_user, login_required
# auth blueprint
from . import auth
# form for registrating form
from .forms import LoginForm, StudentForm
# # used for email sending
# from ..email import mail_message


@auth.route('/register', methods=["GET", "POST"])
def register():
    '''
    geting data from auth form registratin form
    '''
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(username=form.username.data,
                          password=form.password.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('auth.login'))
    title = "New Student Account Details"
    return render_template('auth/register.html',
                           registration_form=form,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Login user after regisatering
    '''
    login_form = LoginForm()

    if login_form.validate_on_submit():
        student = Student.query.filter_by(
            username=login_form.username.data).first()
        if student is not None and student.verify_password(login_form.password.data):
            login_user(student, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "LMS-LITE Login"
    return render_template('auth/login.html',
                           login_form=login_form,
                           title=title)


@auth.route('/logout')
@login_required
def logout():
    '''
    Logout user from session    
    '''
    logout_user()
    return redirect(url_for("main.index"))

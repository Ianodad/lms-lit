from flask import render_template, redirect, url_for, abort, json, request
# settings.py
import os
from config import APP_STATIC, APP_ROOT

# importing main from main blueprint
from . import main
# importing database
from .. import db

# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm
from config import APP_STATIC, APP_ROOT

from .forms import CourseForm, ExerciseForm, AnswersForm

# import models
from ..models import Student, Course, Exercise


from ..content import Courses, Excercise

import random
from random import sample, shuffle


def shuffle(q):
    '''
    shuffles keys of dictionaries
    '''
    listed = ""
    for item in q:
        listed = [*item]

    # shufle words
    shuffled = sample(listed, len(listed))
    return shuffled


# def shuffle(q):
#     """
#     This function is for shuffling
#     the dictionary elements.
#     """
#     selected_keys = []
#     i = 0
#     while i < len(q):
#         current_selection = random.choice(q.keys())
#         if current_selection not in selected_keys:
#             selected_keys.append(current_selection)
#             i = i+1
#     return selected_keys


@main.route('/')
def index():
    '''
    home displays courses and view heading
    '''

    intro = Courses("Computer Intro")
    programming = Courses("Computer programming")
    # course = Courses(course)
    # courses = Course.get_courses()

    return render_template('index.html', intro=intro, programming=programming)


@main.route('/course/intro')
@login_required
def courseintro():
    '''
    displays courses based on when click
    '''
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "static", "content.txt")
    # course = json.load(open(json_url))
    # print(course)
    # course = Course.get_course(id)
    # exercise = Exercise.get_exercise(id)
    intro = Courses("Computer Intro")

    return render_template('courseintro.html', intro=intro)


@main.route('/course/programming')
@login_required
def coursepro():
    '''
    displays courses based on when click
    '''
    pro = Courses("Computer programming")

    return render_template('coursepro.html', pro=pro)


@main.route('/curriculum')
@login_required
def curriculum():
    '''
    contains all courses and exercises for view of teacher
    '''

    courses = Course.get_courses()
    exercises = Exercise.get_exercises()

    return render_template('curriculum.html', courses=courses, exercises=exercises)


@main.route('/exercise/Intro', methods=['GET', 'POST'])
@login_required
def exercise():
    '''
    display exercise of course based on id
    '''

    excercises = Excercise("Intro Excercise")
    questions_shuffled = shuffle(excercises)

    dictionary = ""

    for item in excercises:
        dictionary = item

        return render_template('exerciseintro.html', questions=questions_shuffled, chooses=dictionary)


@main.route('/exercise/programming', methods=['GET', 'POST'])
@login_required
def exerciseintro():
    '''
    display exercise of course based on id
    '''

    excercises = Excercise("Intro Excercise")
    questions_shuffled = shuffle(excercises)

    dictionary = ""

    for item in excercises:
        dictionary = item

        return render_template('exercisepro.html', questions=questions_shuffled, chooses=dictionary)


@main.route('/results/intro', methods=['GET', 'POST'])
@login_required
def quiz_answersintro():
    correct = 0

    excercises = Excercise("Intro Excercise")

    listed = ""
    for item in excercises:
        listed = [*item]
    for i in listed:
        answered = request.form[i]
        print(answered)
        if excercises[0][i][0] == answered:
            correct = correct+1
    return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'


@main.route('/results/programming', methods=['GET', 'POST'])
@login_required
def quiz_answerspro():
    correct = 0

    excercises = Excercise("Programming Excercise")

    listed = ""
    for item in excercises:
        listed = [*item]
    for i in listed:
        answered = request.form[i]
        if excercises[0][i][0] == answered:
            correct = correct+1
    return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

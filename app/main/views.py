from flask import render_template, redirect, url_for, abort, json
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
    courses = Course.get_courses()

    title = 'Home is best'

    return render_template('index.html', title=title, courses=courses)


@main.route('/course')
def course():
    '''
    displays courses based on when click
    '''
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "static", "content.txt")
    # course = json.load(open(json_url))
    # print(course)
    # course = Course.get_course(id)
    # exercise = Exercise.get_exercise(id)
    new = Courses()

    return render_template('course.html', new=new)


@main.route('/courses/add')
def newcourse():
    '''
    prompts user to add new course
    '''

    courseForm = CourseForm()

    if courseForm.validate_on_submit():
        course = courseForm.course.data
        content = courseForm.content.data

        new_course = Course(course=course, content=content)
        new_course.save_course()

        return redirect(url_for('main.curriculum'))

    return render_template('newcourse.html', courseForm=courseForm)


@main.route('/curriculum')
def curriculum():
    '''
    contains all courses and exercises for view of teacher
    '''

    courses = Course.get_courses()
    exercises = Exercise.get_exercises()

    return render_template('curriculum.html', courses=courses, exercises=exercises)


@main.route('/exercise/add/<int:id>')
def newexercise(id):
    '''
    allows teacher to add new exercise
    '''
    exerciseForm = ExerciseForm()

    if exerciseForm.validate_on_submit():
        # exercise = exerciseForm. exercise.data
        question = exerciseForm.question.data
        # answers = exerciseForm.answers.data

        new_exercise = Exercise(question=question, course_id=id)
        new_exercise.save_exercise()

        return redirect(url_for('main.curriculum'))

    return render_template('newexercise.html', title='title', exerciseForm=exerciseForm)


@main.route('/exercise', methods=['GET', 'POST'])
def exercise():
    '''
    display exercise of course based on id
    '''
    excercises = Excercise()
    questions_shuffled = shuffle(excercises)

    dictionary = ""

    for item in excercises:
        dictionary = item
    # answersForm = AnswersForm()
    # if answersForm.validate_on_submit():
    #     answer = exerciseForm.answer.data
    #     new_exercise = Exercise(
    #         answer=answer, exercise_id=id, student_id=current_user.id, course_id=id)
    #     new_exercise.save_exercise()

    # exercise = Exercise.get_exercise(id)

        return render_template('exercise.html', questions=questions_shuffled, chooses=dictionary)

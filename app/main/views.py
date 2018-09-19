from flask import render_template, redirect, url_for, abort
# settings.py
import os
from config import APP_STATIC

# importing main from main blueprint
from . import main
# importing database
from .. import db

# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm

from .forms import CourseForm, ExerciseForm

# import models
from ..models import Student, Course, Exercise
# with open(os.path.join(APP_STATIC, 'content.txt')) as f:
#     content = f.read()

# with open('content.txt', 'r') as f:
#     data = f.readlines()


@main.route('/')
def index():
    '''
    home displays courses and view heading  
    '''
    courses = Course.get_courses()

    title = 'Home is best'

    return render_template('index.html', title=title, courses=courses)


@main.route('/courses/<int:id>')
def course():
    '''
    displays courses based on when click 
    '''

    course = Course.get_course(id)
    exercise = Exercise.get_exercise(id)

    return render_template('course.html', course=course, exercise=exercise)


@main.route('/courses/add')
def newcourse():
    '''
    prompts user to add new course
    '''

    courseForm = CourseForm()

    if courseForm.validate_on_submit():
        title = courseForm.course.data
        content = courseForm.content.data

        new_course = Course(course=title, content=content)
        new_course.save_course()

        return redirect(url_for('main.curriculum'))

    return render_template('newcourse.html', content=content, courseForm=courseForm)


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

    if exercise.validate_on_submit():
        exercise = exerciseForm. exercise.data
        question = exerciseForm.question.data
        answers = eexerciseForm.answers.data

        new_exercise = Exercise(
            exercise=exercise, question=question, answers=answers, course_id=id)
        new_exercise.save_exercise()

        return redirect(url_for('main.curriculum'))

    return render_template('newexercise.html', title='title')


@main.route('/exercise/<int:id>')
def exercise(id):
    '''
    display exercise of course based on id
    '''
    exercise = Exercise.get_exercise(id)
    return render_template('exercises.html', exercise=exercise)

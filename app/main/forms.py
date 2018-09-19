from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required


class CourseForm(FlaskForm):
    '''
    form course 
    '''
    course = StringField('Your title here', validators=[Required()])
    content = TextAreaField('Your content here', validators=[Required()])
    submit = SubmitField('Submit')


class ExerciseForm(FlaskForm):
    '''

    '''
    # exercise = StringField('Your title here', validators=[Required()])
    question = StringField(
        'Whats your question on this topic', validators=[Required()])
    submit = SubmitField('Submit')


class AnswersForm(FlaskForm):
    '''
    anwser to questions
    '''
    answer = StringField('What is you answer', validators=[Required()])

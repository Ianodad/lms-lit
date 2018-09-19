from . import db
from flask_login import UserMixin
# used for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
# passes user id to queries
from . import login_manager

# class Role(db.Model):
# class Teacher(db.Model):


class Student(db.Model):
    '''
    student class model 
    '''
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    courses_id = db.relationship('Courses', backref='student', lazy="dynamic")
    exercise_id = db.relationship(
        'Exercise', backref='student', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Courses(db.Model):
    '''
    Courses model for student
    '''
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    course = db.Column(db.String(255), index=True)
    content = db.Column(db.String(), index=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    # from foreign key
    exercise_id = db.relationship('exercise', backref='course', lazy="dynamic")


class Exercise(db.Model):
    '''
    Exercise
    '''
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer)
    exercise = db.Column(db.String(255))
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

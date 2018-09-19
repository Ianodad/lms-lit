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
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    courses_id = db.relationship('Course', backref='students', lazy="dynamic")
    exercise_id = db.relationship(
        'Exercise', backref='students', lazy="dynamic")

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


class Course(db.Model):
    '''
    Courses model for student
    '''
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    course = db.Column(db.String(255), index=True)
    content = db.Column(db.String(), index=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    # from foreign key
    exercise_id = db.relationship(
        'Exercise', backref='courses', lazy="dynamic")

    def save_course(self):
        '''
        save Courses models to db
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_courses(cls):
        '''
        querys database for a courses by id the returns all id
        '''
        courses = Course.query.order_by('-id').all()
        return courses

    @classmethod
    def get_course(cls, id):
        '''
        querys database for a course
        '''
        course = Course.query.filter_by(id=id).first()
        return course


class Exercise(db.Model):
    '''
    Exercise model
    '''
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer)
    exercise = db.Column(db.String(255))
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    def save_exercise(self):
        '''
        save exercise models to db
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_exercises(cls):
        '''
        querys database for  exercises by id the returns all id
        '''
        exercises = Exercise.query.order_by('-id').all()
        return exercises

    @classmethod
    def get_exercise(cls, id):
        '''
        querys database for an exercise
        '''
        exercise = Exercise.query.filter_by(id=id).first()
        return exercise

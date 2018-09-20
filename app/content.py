import json
import os
import random
from random import sample, shuffle

# from h5py.ipy_completer import readline

from config import APP_ROOT, APP_STATIC


def Courses(course):

    with open(os.path.join(APP_STATIC, 'content.json'), "r") as json_file:
        data = json.load(json_file)
        course = data[course]
    # print(course)
    return course


def Excercise(excercise):

    with open(os.path.join(APP_STATIC, 'excercise.json'), "r") as json_file:
        data = json.load(json_file)
        exi = data[excercise]

    # print(course)
    return exi

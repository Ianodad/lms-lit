import json
import os

# from h5py.ipy_completer import readline

from config import APP_ROOT, APP_STATIC


def Questions():

    with open(os.path.join(APP_STATIC, 'content.json'), "r") as json_file:
        data = json.load(json_file)
        cont = data["Computers"][0]
    # print(course)
    return cont

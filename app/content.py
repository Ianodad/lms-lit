import os

from config import APP_STATIC, APP_ROOT


def Questions():

    with open(os.path.join(APP_STATIC, 'content.txt'), "r") as f:
        content = f.read()

    return content

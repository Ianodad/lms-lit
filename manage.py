from app import create_app, db
# importing script
from flask_migrate import Migrate, MigrateCommand


# script import manger
from flask_script import Manager, Server

# user imports models
from app.models import Student, Exercise, Course

app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)

# difining a manager to app

# access to the shell

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Student=Student, Exercise=Exercise, Course=Course)


# intiate migrate class


if __name__ == '__main__':
    manager.run()

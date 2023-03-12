import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_dir = os.path.normpath(os.path.join(basedir, os.pardir, 'db', 'app.db'))

class Config(object):
    JWT_KEY = os.environ.get('JWT_KEY') or "SUPPOSED_TO_BE_SECRET"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + database_dir
    SQLALCHEMY_TRACK_MODIFICATIONS = False
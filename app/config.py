from environs import Env
from datetime import timedelta

env = Env()
env.read_env()

class Config(object):
    APP_ENV = 'development'
    Debug = True
    FLASK_RUN_HOST = env.str('FLASK_RUN_HOST')
    FLASK_RUN_PORT = env.str('FLASK_RUN_PORT')

    DB_HOST = env.str('DB_HOST', 'localhost')
    DB_USERNAME = env.str('DB_USERNAME', 'root')
    DB_PASSWORD = env.str('DB_PASSWORD', '')
    DB_NAME = env.str('DB_NAME', 'flask_usermanagement')
    DB_PORT = env.str('DB_PORT', '3306')


    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}{DB_PASSWORD}:@{DB_HOST}/{DB_NAME}"

    SECRET_KEY = env.str('SECRET_KEY')

    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)
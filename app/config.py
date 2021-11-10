from environs import Env
from datetime import timedelta

env = Env()
env.read_env()

class Config(object):
    APP_ENV = 'development'
    Debug = True
    FLASK_RUN_HOST = env.str('FLASK_RUN_HOST')
    FLASK_RUN_PORT = env.str('FLASK_RUN_PORT')

    DB_HOST = env.str('DB_HOST', '127.0.0.1')
    DB_USERNAME = env.str('DB_USERNAME', 'root')
    DB_PASSWORD = env.str('DB_PASSWORD', '')
    DB_NAME = env.str('DB_NAME', 'programmer_base')
    DB_PORT = env.str('DB_PORT', '3306')
    MYSQL_UNIX_SOCKET = 'TCP'


    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}{DB_PASSWORD}:@{DB_HOST}/{DB_NAME}"

    SECRET_KEY = env.str('SECRET_KEY', 'ultimate-secr3t-k3y')

    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)
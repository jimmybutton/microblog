import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ka8:4hQY3r3,dv80>9234lgD'

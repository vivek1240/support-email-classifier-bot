import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-t0-guess-this-api-key'
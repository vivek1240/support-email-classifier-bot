import os

from app import app
from configparser import ConfigParser

ROOT_DIR = os.getcwd()
parser = ConfigParser()
parser.read(os.path.join(ROOT_DIR, 'config.ini'))

if __name__ == '__main__':
    if parser.getboolean('other', 'dev_mode'):
        app.run(debug=True, port=parser.getint('other', 'application_port'), host='0.0.0.0')
    else:
        app.run(port=parser.getint('other', 'application_port'), host='0.0.0.0')
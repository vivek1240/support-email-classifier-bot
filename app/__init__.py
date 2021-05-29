import os
from flask import Flask
from config import Config
import pickle
from configparser import ConfigParser

app = Flask(__name__)
app.config.from_object(Config)

ROOT_DIR = os.getcwd()
parser = ConfigParser()
parser.read(os.path.join(ROOT_DIR, 'config.ini'))

MODEL_PATH = os.path.join(ROOT_DIR, 'classificationModel.pkl')
model = None
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

from app import routes
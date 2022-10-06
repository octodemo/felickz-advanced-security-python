import os
import sqlite3

from flask import Flask
from Crypto.Cipher import DES, AES

cipher = DES.new('SECRET_KEY')

def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message)) # BAD: weak encryption

ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES = os.path.join(ROOT, 'templates')

flaskapp = Flask("BookStore", template_folder=TEMPLATES)
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_uri = os.environ.get('SQLITE_URI', ':memory:')

database = sqlite3.connect(database_uri, check_same_thread=False)
cursor = database.cursor()

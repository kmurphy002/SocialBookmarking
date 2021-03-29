import os
import models
import views

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '3C\xc3c\x14\x93x\xd22\x98<\xfbU&\x84\xa8\x9e\xa9M\xc2\x01\x19\xe8\x8e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'SocialBookmarking.db')

db = SQLAlchemy(app)




'''
Created by ZhouSp 18-10-29.
'''

import os
from sayhello import app

__author__ = 'zhou'

dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', dev_db)

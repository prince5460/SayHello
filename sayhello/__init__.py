'''
Created by ZhouSp 18-10-29.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

__author__ = 'zhou'

app = Flask(__name__)
app.config.from_object('sayhello.settings')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True #使用本地bootstrap资源
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from sayhello import views, errors, commands

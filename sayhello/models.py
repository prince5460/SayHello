'''
Created by ZhouSp 18-10-29.
'''
from datetime import datetime

from sayhello import db

__author__ = 'zhou'


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

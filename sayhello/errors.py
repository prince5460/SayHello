'''
Created by ZhouSp 18-10-29.
'''

from flask import render_template

from sayhello import app

__author__ = 'zhou'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

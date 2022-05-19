import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///{}'.format(os.path.join(basedir, 'inventory.db'))

db = SQLAlchemy(app)

import inventory.com.controller.ItemContoller

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
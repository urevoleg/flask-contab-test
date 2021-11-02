# -*- coding: utf-8 -*-
from app import app, api
from app.models import Time


@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!\nIt's flask-contab app test!"


api.add_resource(Time, "/time")

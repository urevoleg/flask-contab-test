# -*- coding: utf-8 -*-
from app import app, api
from app.models import Time
from flask import request

import json


@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!\nIt's flask-contab app test!"


@app.route('/callbacks', methods=['GET', 'POST'])
def spotify():
    return json.dumps(request.args)


api.add_resource(Time, "/time")

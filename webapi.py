#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import control_with_tel
from flask import Flask,render_template
from flask import request
from flask_cors import CORS, cross_origin
from function import control_with_mail,control_with_name,control_with_tel

app = Flask(__name__)
cors = CORS(app)


@app.route('/query', methods=['POST','GET'])
@cross_origin()
def query():

    mail = request.args.get('mail')
    tel = request.args.get('tel')
    name = request.args.get('name')
    
    data = ""

    if mail:
        data = control_with_mail(mail)

    if tel:
        data = control_with_tel(tel)

    if name:
        data = control_with_name(name)

    return data
    


@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(port=1999)

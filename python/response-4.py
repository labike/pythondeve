#重定向响应,使用flask的redirect()方法
flask.redirect(location,code=302,Response=None)

#当用户访问首页时，自动重定向到新手页/newbies
@app.route("/")
def v_index():
	return redirect('/newbies')

@app.route('/newbies')
def v_newbies():
	return 'this page is for newbies only'




# -*- coding:utf-8 -*-
from flask import Flask,redirect,request
app = Flask(__name__)

@app.route('/')
def v_index():
    return redirect('/newbies')
    
@app.route('/newbies')    
def v_newbies():
    return 'this page is for newbies only!'
    
app.run(host='0.0.0.0',port=80)
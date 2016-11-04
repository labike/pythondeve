#读取表单的值
'''
@app.route("/")
def index():
	uid = request.form["uid"]
	pwd = request.form["pwd"]
	return "uid is %s pwd is %s" % (uid,pwd)
'''


# -*- coding:utf-8 -*-
from flask import Flask,request,url_for
app = Flask(__name__)

@app.route('/')
def v_index():
    return  '''
        <form action="/login" method="POST">
        	<input type="text" name="system" placeholder="input your text">
            <input type="text" name="uid" placeholder="input your user id">
            <input type="password" name="pwd" placeholder="input your password">
            <input type="submit" value="Login">
        </form>
    '''
@app.route('/login',methods=['POST'])
def v_login():
  	system = request.form['system']
   	uid = request.form['uid']
   	pwd = request.form['pwd']
    	if system=='CRM' and uid=='admin' and pwd=='123':
        	return 'Authorized successfully!'
    	else:
        	return 'Un-Autorized!'
                
app.run(host='0.0.0.0',port=80)   
#构建json响应,在flask中可以使用json模块的dumps()方法将数组或字典转换为json字符串
from flask import Flask
a = [1,2,3]
print json.dumps(a)
b = {'x':1,'y':2}
print json.dumps(b)

#定义获得用户列表的api为get/user
# -*- coding:utf-8 -*-
from flask import Flask,json
app = Flask(__name__)
users = ['Linda','Marion5','Race8']
@app.route("/user")
def v_user():
	user = ['linda','keven','race5']
	return json.dumps(user),200,[{'Content-Type','application/json;charset=utf-8'}]
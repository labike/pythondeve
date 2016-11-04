#响应response

#1.视图函数返回字符串,当视图函数返回一个字符串时,flask自动使用这个字符串作为正文内容
#以200作为状态码,以text/html作为mimetype,构造一个response对象传递给后续处理环节
@app.route("/ping")
def ping():
	return "pong"
#基于返回结果构造response对象
response:['pong']
status_code:200
mimetype:'text/html'


#2.视图函数返回元祖(response,status,headers)时,flask自动根据这几个值构造一个response对象
@app.route("/")
def index():
	return "pong",200,{"x-tag":"sth.magic"}

#基于返回结果构造response对象
respon:["pong"],
status_code:200
mimetype:"text/html"
headers:{("x-tag","sth.magic")}



#3.视图函数返回response对象,flask直接将此对象用于后续处理
from flask import Flask,make_response
@app.route("/ping")
def index():
	rsp = make_response("pong")
	rsp.mimetype = "text/plain"
	rsp.headers["x-tag"] = "sth.magic"
	return rsp


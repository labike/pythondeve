#终止响应,使用flask框架的abort()方法通知框架终止处理当前响应
flask.abort(code)
#abort()的code参数用来指定返回给客户端的http状态码,由于abort()方法将抛出HttpException异常，因此他后面的代码不会被执行

@app.route('/admin')
def v_admin():
	if 'token' in request.args:
		return 'you are a good boy'
	else:
		abort(401)
#设置cookie,使用flask的set_cookie可以设置客户端cookie
Response.set_cookie(
	key,                  #键
	value='',             #值  
	max_age=None,         #秒为单位的cookie寿命,None表示http-only
	expires = None,       #失效时间,datetime对象或unix时间戳
	path='/',             #cookie的有效路径
	domain=None,          #cookie的有效域
	secure=None,
	httponly=False
)


#访问首页时设置cookie，访问/page2时读取cookie
@app.route("/")
def index():
	rsp = make_response("go <a href='%s'>page2</a>" % '/page2')
	rep.set_cookie('user','JJJJJhonny')
	return rep

@app.route("/page2")
def page2():
	user = request.cookie['user']
	return 'you are %s' % user
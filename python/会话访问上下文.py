#flask框架中,每当一个请求进来时会自动根据请求中的cookie的会话id创建一个session类的实例对象
@app.route('/')
def v_index():
	return request.cookies['session']


#在视图函数内，flask提供了一个全局对象session,他始终等效于当前请求所对应的session类实例对象
#session类定义了get_item()方法和set_item()方法,因此我们可以通过[]操作符读取或设置会话变量
@app.route('/')
if !session['user']:
	return redirect('/login')
return 'some restricted for suthorized users only'

#默认情况下,flask将会话对象加密后存储在客户端的cookie中，因此必须要为应用实例的secret_key属性配置
#一个加密种子才能使用session
app.secret_key = 'sth.random as a entype key'




from flask import Flask,session,request
app = Flask(__name__)
app.secret_key = "wojiaoxiaoming"

@app.route("/")
def index():
	if "count" not in session:
		session["count"] = 0
	session["count"] = session["count"] + 1
	return "this is your %d time visit" % session["count"]

app.run(debug = True)
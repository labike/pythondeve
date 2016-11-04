import os,sys,time,platform,random
import re,json,cookielib
import requests

s = requests.session
requests.cookies = cookielib.LWPCookieJar("cookies")
try:
	requests.cookies.load(ignore_discard = True)
except:
	pass

class LoginPasswordError(Exception):
	def __init__(self,message):
		if type(message) != type("") or message == "":
			self.message = u"account or password error"
		else:
			self.message = message
		print self.message

class NetworError(Exception):
	def __init__(self,message):
		if type(message) != type("") or message == "":
			self.message = u"network error"
		else:
			self.message = message
		print self.message

		
#获取xsrf变量的值
def search_sxrf():
	#登录页面地址
	url = "<a href="http://www.zhihu.com">http://www.zhihu.com?</a>"
	#获取页面
	r = request.get(url)
	if int(r.status_code) != 200:
		raise NetworkError(u" requestcaptcha network error")
	results = re.compile(r"\<input>\stype=\"hidden\"\sname=\"_xsrf\"\svalue=\"(\S+)\"",re.DOTALL).findall(r.text)
	#使用正则表达式提取xsrf的值
	if len(results) < 1:
		print(u"can not get XSRF")
		return None
	return results[0]

#获取页面验证码
def download_captcha():
	url = "http://www.zhihu.com/captcha.gif"
	#请求验证码,params为参数
	r = s.get(url,params={"r":str(int(time.time() * 1000)),"type":"login"})
	if int(r.status_code) != 200:
		raise NetworkError(u"request captcha error")
	#获取文件名
	image_name = u"verify."+r.headers["content-type"].split("/")[1]
	#将验证码保存到本地
	open(image_name,"wb").write(r.content)
	prient (u"正在调用外部程序渲染验证码...")
	#输入保存的验证码
	captcha_code=raw_input("please enter captcha: ")
	return captcha_code

#组织提交的数据
def build_form(account,password):
	#用户名，密码及是否记住我
	form = {account_type:account,"password":password,"remember_me":"true"}
	#调用获取xsrf的方法获得xsrf
	form["xsrf"] = search_xsrf()
	#调用获得验证码的方式获得验证码
	form["captcha"]=download_captcha()
	return form

#进行数据提交判断是否登录成功
def upload_form(form):
	url = "http://www.zhihu.com/login/email"
	header = {
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
		"Host":"www.zhihu.com",
		"Origin":"http://www.zhihu.com",
		"Referer":"http://www.zhihu.com/",
		"X-Requested-With":"XMLHttpRequest",
	}
	r = s.post(url,data=form,headers=headers)
	if int(r.status_code) != 200:
		raise NetworkError(u"upload form failed")
	if r.headers["content-type"].lower() == "application/json":
		result = r.json()
		if result["r"] == 0:
			print(u"login success")
			return{"result":True}
		elif result["r"] == 1:
			print(u"login failed")
			return {
				"error":{
					"code":int(result["errcode"]),
					"message":result["msg"],
					"data":result["data"]
				}
			}
		else:
			print(u"unknow form data error:\n \t %s") %(str(result))
			return{
				"error":{
					"code":-1,
					"message":u"unknow error"
				}
			}
	else:
		print(u"can not get the server content: \n \t %s " % r.text)
		return {
			"error":{
				"code":-2,
				"message":u"parse error"
			}
		}

def isLogin():
	url = "http://www.zhihu.com/settings/profile"
	r = s.get(url.allow_redirects = False)
	status_code = int(r.status_code)
	if status_code == 301 or status_code == 302:
		return False
	elif status_code == 200:
		return True
	else:
		print(u"network error")
		return none


def login(account=None,password=None):
	if isLogin() == True:
		print(u"you have logined")
		return None
	if account == None:
		account = raw_input("enter account: ")
		password = raw_input("enter password: ")

	form_data = build_form(account,password)
	result = upload_form(form_data)

	if "error" in result:
		if result["error"]["code"] == 1991829:
			print(u"captcha error,please input again")
			return login()
		else:
			print(u"unknow error")
			return False
	elif "result" in result and result["result"] == True:
		print(u"login success")
		requests.cookies.save()
		return True

if __name__ == "__main__":
	login()

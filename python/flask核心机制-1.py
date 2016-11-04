#flask框架对request对象的构造和分发处理过程是分离的，两个过程通过一个全局性的栈关联起来
#从而产生一个栈顶的请求上下文概念
#flask并发通过线程、协程的本地存储机制实现的







1.wsgi  web服务器网关接口是为python定义的web服务器和web应用程序之间的一种简单通用的接口
'''
实现一个wsgi应用需要满足三个要求:
1.是可调用的，比如一个函数，或者一个可调用类(具有__call__方法)的实例
2.wsgi应用应当返回一个可迭代(iterable)的值,比如字符串列表
3.wsgi应用在返回之前，应当调用wsgi服务器传入的start_response函数发送状态码和http报文头
'''

最小的wsgi应用
from wsgiref.simple_server import make_server

def wsgi_app(enviror,start_respon):        #enviror是一个包含全部http请求信息的字典/dict,由wsgi服务器解包http请求生成
	start_response('200 ok',[('Context-Type','text/plain')])
	return 'such a tiny wsgi app!'

httpd = make_server('0.0.0.0',80,wsgi_app)
httpd.server_forever()



2.使用类实现wsgi应用
class WSGI_APP:
	def __call__(self,environ,start_response):
		start_response('200 ok',[('Context-Type','text/plain')])
		return 'such a tiny wsgi app!'
app = WSGI_APP()


from wsgiref.simple_server import make_server
class WSGI_APP:
	def __call__(self,environ,start_response):
		start_response('200 ok',[('Context-Type','text/plain')])
		return 'such a tiny wsgi app'

app = WSGI_APP()
httpd = make_server('0.0.0.0',80,app)
print 'start server'
httpd.server_forever()







3.flask处理流程

a.创建上下文对象,包括当前http请求信息的RequestContext对象和当前应用的Appcontext对象
RequestContext对象内主要包含两个和请求信息相关的对象,request对象基本是基于wsgi服务器传入的环境变量environ的封装
它表征了来自客户端的全部信息,session对象则是根据请求中的cookie，重新载入该访问者相关的会话信息
AppContext对象主要提供给用户一次请求周期内有效的存储空间,比如g

b.入栈,将两个上下文对象分别推入两个全局堆栈:_request_ctx_stack和_app_ctx_stack

c.请求分发,调用dispatch_request()函数处理_request_ctx_stack栈顶的对象,也就是我们刚刚推入的RequestContext对象
dispathch_request()所做的主要工作就是根据http请求的url信息，通过路由表找到并调用视图函数进行处理
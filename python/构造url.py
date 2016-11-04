#硬编码
@ap.route("/")
def v_index():
	return "<a href='/tech'>tech</a>"
@app.route("/tech")
def v_tech():
	pass

#使用访问点
@app.route("/")
def v_index():
	print url_for("v_contacts")
	return "see console output!"
@app.route("/contact")
def v_contacts():pass

#添加查询参数,使用关键字参数，可以在构造的url中生成查询串,下面的调用将生成/contact?format=json
@app.route("/")
def v_index():
	print url_for("v_contacts",format="json")
	return ""

@app.route("/contact")
def v_contacts():pass

#添加url变量,如果指定访问点对应的驶入函数接收参数,那么关键字参数将生成对应的参数url
#下面将生成/contact/julia?format=html
@app.route("/")
def v_index():
	print url_for("v_contact",name="julia",format="html")
	return ""

@app.route("/contact/<name>")
def v_contacts():pass


#添加锚点,使用_anchor关键字可以为生成的url添加锚点,下面的示例将生成/contact#part2
@app.route("/")
def v_index():
	print url_for("v_contacts",_anchor="part2")

app.route("/contact")
def v_contacts():pass


#外部url,默认情况下，url_for生成站内url,可以设置关键字_external为true生成包含站点地址外的
#下面将生成http://xxx/contact:
@app.route("/")
def v_index():
	print url_for("v_contacts",_external=True)

@app.route("/contact")
def v_contacts():pass


# -*- coding:utf-8 -*-
from flask import Flask,url_for
app = Flask(__name__)
@app.route('/')
def v_index():
    print url_for('v_contact',format='json&page=1')
    print url_for('v_contact',name='Julia')
    print url_for('v_contact',name='Julia',ret='json')
    print url_for('v_contact',name='Julia',_external=True)
    print url_for('v_contact',name='Julia',_external=True,_scheme='https')
    print url_for('v_contact',name='Julia',_anchor='photo')
    print url_for('v_contact',name='whoami',format='xml')
    return 'see console output!'


@app.route('/contact',methods=['POST','GET'])
def v_contacts():pass
  

@app.route('/contact/<name>')
def v_contact(name):pass



app.run(host='0.0.0.0',port=80)

输出:
/contact?json&page=1
/contact/Julia
/contact/Julia/ret=json
http://xxx.com/contact/Julia
https://xxx.com/contact/Julia
/contact/Julia#photo
/contact/whoami?format=xml
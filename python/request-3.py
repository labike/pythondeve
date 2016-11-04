#读取查询参数
@app.route("/")
def search():
	q = request.args[q]
	return "your are searching %s" % q



# -*- coding:utf-8 -*-
from flask import Flask,request,url_for
app = Flask(__name__)
@app.route('/')
def v_index():
    return '''
        <form method="GET" action="/search">
        	<input type="text" name="page" placeholder="input page numb">
            <input type="text" placeholder="input keywords" value="Python Flask" name="q">
            <input type="submit" value="search">
        </form>
    '''    
@app.route('/search')          
def v_search():
    if 'q' in request.args:
        ret = '<p>searching %s...</p>' % request.args['q']
    else:
        ret = 'what do you want to search?'
        return ret
    page = request.args["page"]
    return page
    
  		

app.run(host='0.0.0.0',port=80)
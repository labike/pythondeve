#读取json数据
$.ajax({
	url:"/user",
	method:"POST",
	data:JSON.stringify(jsondata),
	contentType:"application/json,charset=UTF-8",
	sucess:function(){},
	error:function(){}
});

@app.route("/")
def index():
	print request.json
	return 



# -*- coding:utf-8 -*-
from flask import Flask,request,json
app = Flask(__name__)
@app.route('/')
def v_index():
    return  '''
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
        </head>
        <body>
            <form id="test">
                <input type="text" name="name" placeholder="contact name">
                <input type="text" name="tel" placeholder="contact telephone">
                <input type="submit" value="Ajax POST">
            </form>
            <div id="status"></div>
            <script>
                $(function(){
                    $("form#test").submit(function(){
                        var data = $("form#test").serializeArray();
                        var jsondata = {}
                        data.forEach(function(d){jsondata[d.name] = d.value});
                        $.ajax({
                            url : "/user",
                            method : "POST",
                            data : JSON.stringify(jsondata),
                            contentType : "application/json;charset=UTF-8",
                            success : function(dt,er,xhr){
                                $("#status").text(dt);
                            },
                            error : function(){}
                        });
                        return false;
                    });
                })
            </script>
        </body>
        </html>
    '''
users = []    
@app.route('/user',methods=['POST'])
def v_user():
    users.append(request.json)
    return json.dumps(users)
    
app.run(host='0.0.0.0',port=80)
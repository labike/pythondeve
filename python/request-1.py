#如何访问request对象
from flask import Flask
@app.route("/")
def index():
	print request.headers
	print request.cookies
	return

app.run(debug = True)
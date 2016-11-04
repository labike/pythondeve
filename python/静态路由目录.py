'''
/app
	/web.py
	/static
		/main.css
		/jquery.min.js
'''
#改变默认的本地路径,用static_folder改变默认的静态文件夹
app = Flask(__name__,static_folder="assets")
app = Flask(__name__,static_folder="/var/www/static")

#改变默认的url规则,用static_url_path
app = Flask(__name__,static_folder="assets",static_url_path="/assets")


'''
flask内部用两张表维护路由:
	url_map:维护url规则和endpoint的映射
	view_functions:维护endpoint和视图函数

'''
#自定义访问点
@app.route("/home",endpoint="whocare")
def home():pass

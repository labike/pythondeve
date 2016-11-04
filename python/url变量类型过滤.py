'''
url变量类型过滤
/var 
	/readonly
		/a.txt
		/b.txt
		/repo
			/c.txt
			/d.txt

通过http共享文件夹/var/readonly中的文件
'''
@app.route("/file/<fname>")
def v_file(fname):
	fullname = os.path.join("/var/readonly",fname)
	f = open(fullname)
	cnt = f.read()
	f.close()
	return cnt

#上面url无法读取/repo下面的文件,是因为默认情况下,在url规则中的变量被视为不包含/的字符串
@app.route("/file/<path:fname>")

#计算两个数的值
@app.route("/add/<path:args>")
def add(args):
	return str(sum([int(arg) for arg in args.split("/")]))


@app.route("/add/<int:args1>/<int:args2>")
def add(args1,args2):
	return str(args1 + args2)

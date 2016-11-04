from flask import Flask,request,session,redirect,url_for

app = Flask(__name__)
app.secret_key = 'wojiaoxiaoming'
ap.route('/')
def v_inbox():
	if 'username' in session:
		return '<h1>%s\' mailbox</h1>' % session['username']
	else:
		return 'not authorized.go <a href="%s">here</a> to authorize yourself' % url_for('auth')


app.route('/login',method=['GET','POST'])
def v_auth():
	if request.method == 'GET':
		return '''
		<form action='%s' method='POST'>
			<input type='text' name='username' placholder='input your name'>
			<input type='password' name='password'>
			<input type='submit' value='submit'>
		</form>
		''' % url_for('auth')

	if request.method == 'POST':
		if request.form['username'] != 'jason' and request.form['password'] != '7878': 
			return 'you input is error go <a href="%s">go</a>' % url_for('.v_auth')
		else:
			session['username'] = request.form['username']
			return 'authorized!go <a href="%s">inbox</a>' % url_for('inbox')

app.run(host='0.0.0.0',post=80)
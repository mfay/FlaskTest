from flask import Flask, render_template, session, url_for, redirect, flash, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # os.environ['SECRET'] if os.environ.has_key('SECRET') else 'replace me!!!'

db = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD'] 
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB'] 
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST'] 

db.init_app(app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/env")
def env():
	return os.environ['MYSQL_DATABASE_HOST'] 

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('logged_in', False)
	flash('Hello.  You are not logged in.')
	return redirect(url_for('index'))

@app.route("/login_post", methods=['POST'])
def login_post():
	session['username'] = request.form['username']
	session['logged_in'] = True
	flash('Hello.  You are now logged in.')
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()

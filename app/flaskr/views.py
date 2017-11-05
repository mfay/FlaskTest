from flaskr import app
from flask import Flask, render_template, session, url_for, redirect, flash, request 
from flaskr.models import User
from flaskr.database import db_session

@app.route('/')
def index():
	return render_template('index.html', users=User.query.all())

@app.route('/new', methods=['GET', 'POST'])
def new():
	if request.method == 'GET':
		return render_template('new.html')
	else:
		u = User()
		u.firstName = request.form['firstName']
		u.lastName = request.form['lastName']
		u.email = request.form['email']
		db_session.add(u)
		db_session.commit()
		flash('New user created.')
		return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
	u = User.query.filter(User.id == id).first()
	db_session.delete(u)
	db_session.commit()
	return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
	u = db_session.query(User).filter_by(id = id).first()
	if request.method == 'GET':
		return render_template('edit.html', user=u)
	else:
		u.firstName = request.form['firstName']
		u.lastName = request.form['lastName']
		u.email = request.form['email']
		flash('User updated')
		db_session.commit()
		return redirect(url_for('index'))

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

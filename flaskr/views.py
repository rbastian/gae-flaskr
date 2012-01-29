__author__ = 'rbastian'

from flask import Flask, request, session, g, redirect, url_for,\
    abort, render_template, flash
from flaskr import app
from models import Post

#@app.before_request
#def before_request():
#    g.db = connect_db()

#@app.teardown_request
#def teardown_request(exception):
#    g.db.close()

@app.route('/')
def show_entries():
    posts = Post.all()
    return render_template('show_entries.html', entries=posts)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
#    g.db.execute('insert into entries (title, text) values (?, ?)',
#        [request.form['title'], request.form['text']])
#    g.db.commit()

    post = Post(title=request.form['title'], content=request.form['text'])
    post.put()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


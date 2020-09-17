 
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'prettyprinted'

@app.route('/')
def index():
    print("session"+session['mode'])
    return render_template('index.html')

@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode'] = mode
    print(session['mode'])
    return redirect(url_for('index'))

@app.route('/drop-session')
def drop_session():
    session.pop('mode', None)
    print(session["111"+'mode'])
    return redirect(url_for('index'))

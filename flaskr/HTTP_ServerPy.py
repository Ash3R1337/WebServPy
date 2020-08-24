from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
import sqlite3
#Configuration 
DATABASE = '/tmp/flaskr.db'
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'Ash3R'
PASSWORD = '123'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=False,
    SECRET_KEY='development key',
    USERNAME='Ash3R',
    PASSWORD='123'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
@app.route("/index")
def Index():
    return render_template("index.html", title = 'Ash3RPage')


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4567)
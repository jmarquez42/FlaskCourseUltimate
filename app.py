from flask import Flask, jsonify, request, render_template, redirect, url_for, g
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'holamundo'


def connect_db():
    sql = sqlite3.connect('C:\Users\jmarquez\PycharmProjects\FlaskCourseUltimate\db\data.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    print(g)
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['POST', 'GET'], defaults={'name': 'Usuario'})
@app.route('/<name>', methods=['POST', 'GET'])
def index(name):
    return render_template('home.html', name=name)

@app.route('/json')
def jsonh():
    return jsonify({'name': 'Jose', 'edad': 30})

@app.route('/query')
def query():
    name = request.args.get('name')
    print(name)
    return '<h1>Hello {} </h1>'.format(name)

@app.route('/forms', methods= ['GET','POST'])
def forms():
    if request.method == 'GET':
        return render_template('forms.html')
    else:
        name = request.form['name']
        location = request.form['location']
        return redirect(url_for('process'), name=name, location=location)


@app.route('/process',  methods=['POST', 'GET'])
def process():
    name = request.form['name']
    loca = request.form['location']
    return '<h1>Hello {}, {} </h1>'.format(name, loca)

@app.route('/processjson',  methods=['POST', 'GET'])
def processjson():
    data = request.get_json()
    name = data['name']
    loca = data['location']
    return jsonify({'name': name, 'location': loca})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return '<h1>Hello {} </h1>'.format(name)

@app.route('/json')
def jsonh():
    return jsonify({'name': 'Jose', 'edad': 30})

if __name__ == '__main__':
    app.run()
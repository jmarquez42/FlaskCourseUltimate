from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'], defaults={'name': 'User'})
@app.route('/<name>', methods=['POST', 'GET'])
def index(name):
    n = name
    print(n)
    return '<h1>Hello {} </h1>'.format((n))

@app.route('/json')
def jsonh():
    return jsonify({'name': 'Jose', 'edad': 30})

@app.route('/query')
def query():
    name = request.args.get('name')
    print(name)
    return '<h1>Hello {} </h1>'.format(name)

@app.route('/forms')
def forms():
    form = '''
        <form method="POST" action="/process">
            <input type="text" name="name"/>
            <input type="text" name="location"/>
             <input type="submit" value="Enviar"/>
        </form>
    '''
    return form


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
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/teste', methods=['GET'])
def teste():
    return Response("{'message':'TESTE'}", status=200, mimetype='application/json')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5020)

app.run()

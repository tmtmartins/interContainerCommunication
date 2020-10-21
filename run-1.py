from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def teste():
    return Response('FUNCIONANDO')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5020)

app.run()

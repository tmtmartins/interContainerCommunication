from flask import Flask
from flask import Response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chamar():
    response = requests.get('http://api-teste1')
    print(response)
    return(response)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)

app.run()

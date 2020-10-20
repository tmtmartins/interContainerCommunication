from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/', methods = ['POST'])
    response = requests.post(url="http://0.0.0.0:5000/teste")
    print(response)
    return response

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)
    
app.run()

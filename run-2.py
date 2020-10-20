from flask import Flask
from flask import Response
from flask import Request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def chamar():
    response = requests.post(url="http://172.22.0.1:5020/")
    print(response)
    return response

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)
    
app.run()

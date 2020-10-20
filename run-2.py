from flask import Flask
from flask import Response, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chamar():
    #response = request.post(url="http://0.0.0.0:5020/")
    #print(response)
    return redirect("http://0.0.0.0:5020/", 'teste-api')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)

app.run()

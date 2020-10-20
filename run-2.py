from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def chamar():
    response = request.get(api-teste1)
    print(response)
    return(response)
    #return redirect(api-teste1, code=302)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)

app.run()

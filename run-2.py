from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chamar():
    return redirect("api-teste1", code=302)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5021)

app.run()

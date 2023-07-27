from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Hello I'm Python Server"

@app.route('/test')
def test():
    return "Hello I'm test block"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
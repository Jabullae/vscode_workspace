from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/busan')
def amu():
    return '역시 부산아인교!'

if __name__ == "__main__":
    app.run()
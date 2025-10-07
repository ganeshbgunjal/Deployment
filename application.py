from flask import Flask, request, jsonify


application = Flask(__name__)
app = application

@app.route('/')
def hello_wold():
    return '<h1>Hello Python World </h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
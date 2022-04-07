from flask import Flask, jsonify

myapp = Flask(__name__)

@myapp.route('/', methods=['GET'])
def index():
    return "hello"

if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
import json

from flask import Flask


app = Flask(__name__)


@app.route('/xxx/yy')
def home():
    return '欢迎使用'


@app.route('/to/info')
def play():
    info = {'code': 1000, 'data': [11, 22 ,33]}
    data_string = json.dumps(info)
    return data_string


if __name__ == '__main__':
    app.run()
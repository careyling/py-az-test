from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from blob_conn import blob_data_command
from db_conn import db_data_command

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    datas = blob_data_command.db_data_selectall()
    #datas = db_data_command.db_data_selectall()
    return render_template('list.html', route="blobtest")


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
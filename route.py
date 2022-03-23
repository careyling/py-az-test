from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for
import blobtest
import dbtest

myapp = Flask(__name__)

datas = [{"name":'dbtest',"link":'/dbtest'},{"name":'blobtest',"link":'/blobtest'}]

def index():
    return render_template('index.html', menulist=datas)

# list
myapp.add_url_rule("/",endpoint="index",view_func=index, methods=['GET'])

myapp.add_url_rule("/dbtest",endpoint="dbtest",view_func=dbtest.index, methods=['GET'])
myapp.add_url_rule("/dbtest.SEARCH",endpoint="dbtest_search",view_func=dbtest.search, methods=['GET'])
myapp.add_url_rule("/dbtest.SEARCHONE/<id>",endpoint="dbtest_search_one",view_func=dbtest.search_one, methods=['GET'])
myapp.add_url_rule("/dbtest.FIX",endpoint="dbtest_fix_data",view_func=dbtest.fix_data, methods=['POST'])
myapp.add_url_rule("/dbtest.DEL/<id>",endpoint="dbtest_del_data",view_func=dbtest.del_data, methods=['POST'])

myapp.add_url_rule("/blobtest",endpoint="blobtest",view_func=blobtest.index, methods=['GET'])
myapp.add_url_rule("/blobtest.SEARCH",endpoint="blobtest_search",view_func=blobtest.search, methods=['GET'])
myapp.add_url_rule("/blobtest.SEARCHONE/<id>",endpoint="blobtest_search_one",view_func=blobtest.search_one, methods=['GET'])
myapp.add_url_rule("/blobtest.FIX",endpoint="blobtest_fix_data",view_func=blobtest.fix_data, methods=['POST'])
myapp.add_url_rule("/blobtest.DEL/<id>",endpoint="blobtest_del_data",view_func=blobtest.del_data, methods=['POST'])

# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
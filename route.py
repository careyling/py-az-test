from flask import Flask, render_template
import blobtest
import dbtest
import dbvalue
import converttest

myapp = Flask(__name__)

datas = [{"name":'blobtest',"link":'/blobtest'},{"name":'converttest',"link":'/converttest'},{"name":'dbtest',"link":'/dbtest'},{"name":'dbvalue',"link":'/dbvalue'}]

def index():
    return render_template('index.html', menulist=datas)

# list
myapp.add_url_rule("/",endpoint="index",view_func=index, methods=['GET'])

myapp.add_url_rule("/blobtest",endpoint="blobtest",view_func=blobtest.index, methods=['GET'])
myapp.add_url_rule("/blobtest.SEARCH",endpoint="blobtest_search",view_func=blobtest.search, methods=['GET'])
myapp.add_url_rule("/blobtest.SEARCHONE/<id>",endpoint="blobtest_search_one",view_func=blobtest.search_one, methods=['GET'])
myapp.add_url_rule("/blobtest.FIX",endpoint="blobtest_fix_data",view_func=blobtest.fix_data, methods=['POST'])
myapp.add_url_rule("/blobtest.DEL/<id>",endpoint="blobtest_del_data",view_func=blobtest.del_data, methods=['POST'])

myapp.add_url_rule("/converttest",endpoint="converttest",view_func=converttest.index, methods=['GET'])

myapp.add_url_rule("/dbtest",endpoint="dbtest_search",view_func=dbtest.search, methods=['GET'])

myapp.add_url_rule("/dbvalue",endpoint="dbvalue",view_func=dbvalue.index, methods=['GET'])
myapp.add_url_rule("/dbvalue.SEARCH",endpoint="dbvalue_search",view_func=dbvalue.search, methods=['GET'])
myapp.add_url_rule("/dbvalue.SEARCHONE/<id>",endpoint="dbvalue_search_one",view_func=dbvalue.search_one, methods=['GET'])
myapp.add_url_rule("/dbvalue.FIX",endpoint="dbvalue_fix_data",view_func=dbvalue.fix_data, methods=['POST'])
myapp.add_url_rule("/dbvalue.DEL/<id>",endpoint="dbvalue_del_data",view_func=dbvalue.del_data, methods=['POST'])


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
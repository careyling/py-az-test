from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from models import TestModel_BlobData

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    return render_template('list.html', route="blobtest")


@myapp.route('/blobtest.SEARCH', methods=['GET'])
def search():
    try:
        #[{'ID': 1, 'V1': 2, 'V2': 3}]
        datas = TestModel_BlobData.searchAll()        
        return json.dumps(datas)
        #return render_template('list.html', result=datas,route="blobtest")
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/blobtest.SEARCHONE/<id>', methods=['GET'])
def search_one(id):
    try:
        data = TestModel_BlobData.searchOne(id)
        id = data[0]
        v1 = data[1]
        v2 = data[2]
        return jsonify({'ID': id,'V1': v1,'V2': v2})
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/blobtest.FIX', methods=['POST'])
def fix_data():
    newdata = request.form['newdata']
    id = request.form['id']
    v1 = request.form['v1']
    v2 = request.form['v2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        if newdata == "true":
            act = TestModel_BlobData.insert(data)
        else:
            act = TestModel_BlobData.update(data)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/blobtest.DEL/<id>', methods=['POST'])
def del_data(id):
    try:
        act = TestModel_BlobData.delete(id)        
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
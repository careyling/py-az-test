from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from models import TestModel_DbData

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

myapp = Flask(__name__)

# 测试数据暂时存放
#tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    return render_template('list.html', route="dbtest")


@myapp.route('/dbtest.SEARCH', methods=['GET'])
def search():
    try:
        #[('1', '2', '3'), ('2', '3', '4'), ('3', '4', '5'), ('4', '5', '6')]
        datas = TestModel_DbData.searchAll()
        return json.dumps(datas)
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/dbtest.SEARCHONE/<id>', methods=['GET'])
def search_one(id):
    try:
        data = TestModel_DbData.searchOne(id)
        id = data[0]
        v1 = data[1]
        v2 = data[2]
        return jsonify({'ID': id,'V1': v1,'V2': v2})
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/dbtest.FIX', methods=['POST'])
def fix_data():
    newdata = request.form['newdata']
    id = request.form['id']
    v1 = request.form['v1']
    v2 = request.form['v2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        if newdata == "true":
            act = TestModel_DbData.insert(data)
        else:
            act = TestModel_DbData.update(data)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/dbtest.DEL/<id>', methods=['POST'])
def del_data(id):
    try:
        act = TestModel_DbData.delete(id)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
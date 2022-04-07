from flask import Flask, request, jsonify, render_template, json

from models import TestValueModel

myapp = Flask(__name__)

# 测试数据暂时存放
#tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    return render_template('list.html', route="dbvalue")


@myapp.route('/dbvalue.SEARCH', methods=['GET'])
def search():
    try:
        #[('1', '2', '3'), ('2', '3', '4'), ('3', '4', '5'), ('4', '5', '6')]
        datas = TestValueModel.searchAll()
        return json.dumps(datas)
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/dbvalue.SEARCHONE/<id>', methods=['GET'])
def search_one(id):
    try:
        data = TestValueModel.searchOne(id)
        id = data[0]
        v1 = data[1]
        v2 = data[2]
        return jsonify({'ID': id,'V1': v1,'V2': v2})
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/dbvalue.FIX', methods=['POST'])
def fix_data():
    newdata = request.form['newdata']
    id = request.form['id']
    v1 = request.form['v1']
    v2 = request.form['v2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        if newdata == "true":
            act = TestValueModel.insert(data)
        else:
            act = TestValueModel.update(data)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/dbvalue.DEL/<id>', methods=['POST'])
def del_data(id):
    try:
        act = TestValueModel.delete(id)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
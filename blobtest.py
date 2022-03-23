from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from blob_conn import blob_data_command

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    #datas = db_data_command.db_data_selectall()
    return render_template('list.html', route="blobtest")


@myapp.route('/blobtest.SEARCH', methods=['GET'])
def search():
    try:
        #datas = blob_data_command.db_data_selectall()        
        return json.dumps(tasks)
        #return render_template('list.html', result=datas,route="blobtest")
    except Exception as e:
        err = str(e)
        return err 



@myapp.route('/blobtest.SEARCHONE/<id>', methods=['GET'])
def search_one(id):
    try:
        #data = blob_data_command.db_data_selectone(id)
        data = tasks[0]        
        id = data[0]
        v1 = data[1]
        v2 = data[2]
        return jsonify({'ID': id,'V1': v1,'V2': v2})
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/blobtest.UPD/<id>', methods=['POST'])
def fix_data():
    newdata = request.form['newdata']
    id = request.form['id']
    v1 = request.form['v1']
    v2 = request.form['v2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        if newdata == "true":
            act = blob_data_command.db_data_add(data)
        else:
            act = blob_data_command.db_data_upd(data)
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/blobtest.DEL/<id>', methods=['POST'])
def del_data(id):
    try:
        act = blob_data_command.db_data_del(id)        
        return jsonify({'ACT': act})
    except Exception as e:
        err = str(e)
        return err


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
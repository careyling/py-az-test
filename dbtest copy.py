from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from db_conn import db_data_command

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

myapp = Flask(__name__)

# # 测试数据暂时存放
# tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    #datas = db_data_command.db_data_selectall()
    return render_template('mainlist.html', route="dbtest")


@myapp.route('/dbtest.SEARCH', methods=['GET'])
def search():
    try:
        datas = db_data_command.db_data_selectall()
        return render_template('mainlist.html', result=datas,route="dbtest")
    except Exception as e:
        err = str(e)
        return err 


@myapp.route('/dbtest.ADD', methods=['GET'])
def add_form():
    return render_template('mainframe.html')


@myapp.route('/dbtest.ADD', methods=['POST'])
def add_data():
    id = request.form['ID']
    v1 = request.form['V1']
    v2 = request.form['V2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        db_data_command.db_data_add(data)
        return redirect(url_for('search'))
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/dbtest.UPD/<id>', methods=['GET'])
def upd_form(id):
    try:
        data = db_data_command.db_data_selectone(id)
        return render_template('mainframe.html', 
            ID=data[0],
            V1=data[1],
            V2=data[2]
        )
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/dbtest.UPD/<id>', methods=['POST'])
def upd_data(id):
    id = request.form['ID']
    v1 = request.form['V1']
    v2 = request.form['V2']
    str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
    data = eval(str)
    try:
        act = db_data_command.db_data_upd(data)
        if act:
            return redirect(url_for('search'))
        else:
            return False
    except Exception as e:
        err = str(e)
        return err


@myapp.route('/dbtest.DEL/<id>', methods=['POST'])
def del_data(id):
    try:
        act = db_data_command.db_data_del(id)
        if act:
            return redirect(url_for('search'))
        else:
            return False
    except Exception as e:
        err = str(e)
        return err


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
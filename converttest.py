from flask import Flask, abort, request, jsonify, render_template, json,redirect,url_for

from models import TestModel_BlobData,TestModel_DbData

myapp = Flask(__name__)

# 测试数据暂时存放
tasks = [('1', '2', '3'), ('2', '3', '4')]

@myapp.route('/', methods=['GET'])
def index():
    try:
        datas = TestModel_BlobData.searchAll()
        if len(datas) == 0:
            return json.dumps("NULL")
        for data in datas:
            id = data[0]
            v1 = data[1]
            v2 = data[2]
            str = "{'ID':"+id+",'V1':"+v1+",'V2':"+v2+"}"
            edata = eval(str)
            TestModel_DbData.insert(data=edata)
            TestModel_BlobData.delete(id)
        return json.dumps("OK")
    except Exception as e:
        err = str(e)
        return err 


# 起動用
if __name__ == '__main__':
    myapp.run(debug=True, host='127.0.0.1', port=5000)
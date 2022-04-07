import sys,os
sys.path.append(os.getcwd())
from db_conn import db_conn_command

oralce_conn = db_conn_command.OracleDatabase()

def searchAll():
    try:
        sql = "SELECT ID,V1,V2 FROM TESTVALUE ORDER BY ID"
        datas = oralce_conn.selectall(sql=sql,param=None)
        return datas
    except Exception as e:
        raise e


def searchOne(id):
    try:
        sql = "SELECT ID,V1,V2 FROM TESTVALUE WHERE ID = :id"
        param = {'id': id}
        data = oralce_conn.selectone(sql=sql,param=param)
        return data
    except Exception as e:
        raise e


def insert(data):
    try:
        ID = str(data["ID"])
        V1 = str(data["V1"])
        V2 = str(data["V2"])
        param = (ID, V1, V2)
        sql = "INSERT INTO TESTVALUE VALUES(:1,:2,:3)"
        rcount = oralce_conn.exec(sql=sql,param=param)
        return rcount
    except Exception as e:
        raise e


def update(data):
    try:
        ID = str(data["ID"])
        V1 = str(data["V1"])
        V2 = str(data["V2"])
        param = {'id': ID, 'v1': V1, 'v2': V2}
        sql = "UPDATE TESTVALUE SET V1 = :v1, V2 = :v2 WHERE ID=:id"
        rcount = oralce_conn.exec(sql=sql,param=param)
        return rcount
    except Exception as e:
        raise e


def delete(id):
    try:
        sql = "DELETE TESTVALUE WHERE ID = :id"
        param = {'id': id}
        rcount = oralce_conn.exec(sql=sql,param=param)
        return rcount
    except Exception as e:
        raise e

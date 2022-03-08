# load .env
import cx_Oracle

from dotenv import load_dotenv, find_dotenv
load_dotenv(verbose=True)

import os

TARGET_HOST = os.environ['TARGET_HOST']
PORT = os.environ['PORT']
SERVICE_NAME = os.environ['SERVICE_NAME']
USERNAME = os.environ['DBUSERNAME']
PASSWORD = os.environ['DBPASSWORD']

def db_connect():
    try:
        tns = cx_Oracle.makedsn(TARGET_HOST, PORT, SERVICE_NAME)  # tnsを設定
        conn = cx_Oracle.connect(USERNAME, PASSWORD, tns)  # DBに接続
        # tns = cx_Oracle.makedsn('dx.huangyi.cn','1521','ORCL')  # tnsを設定
        # conn = cx_Oracle.connect('C##VCC', 'VCC', tns)  # DBに接続
        # conn = cx_Oracle.connect('C##VCC', 'VCC', 'dx.huangyi.cn:1521/ORCL')
        return conn
    except Exception as e:
        raise e


def db_connect_close(conn):
    conn.close()  # DB　クローズ


def db_data_selectall():
    try:
        conn = db_connect()
        cur = conn.cursor()  # カーソルを取得

        sql = "SELECT ID,V1,V2 FROM TESTDATA ORDER BY ID"

        cur.execute(sql)
        rows = cur.fetchall()  # カーソルからデータの取得

        cur.close()  # カーソル クローズ
        db_connect_close(conn)
        return rows
    except Exception as e:
        raise e


def db_data_selectone(id):
    conn = db_connect()
    cur = conn.cursor()  # カーソルを取得

    sql = "SELECT ID,V1,V2 FROM TESTDATA WHERE ID = :id"
    param = {'id': id}

    cur.execute(sql, param)
    row = cur.fetchone()  # カーソルからデータの取得

    cur.close()  # カーソル クローズ
    db_connect_close(conn)
    return row


def db_data_add(data):
    ID = str(data["ID"])
    V1 = str(data["V1"])
    V2 = str(data["V2"])
    sql = "INSERT INTO TESTDATA VALUES(:1,:2,:3)"
    param = (ID, V1, V2)

    conn = db_connect()
    cur = conn.cursor()  # カーソルを取得

    cur.execute(sql, param)
    conn.commit()

    cur.close()  # カーソル クローズ
    db_connect_close(conn)

    return True

def db_data_upd(data):
    ID = str(data["ID"])
    V1 = str(data["V1"])
    V2 = str(data["V2"])
    sql = "UPDATE TESTDATA SET V1 = :v1, V2 = :v2 WHERE ID=:id"
    param = {'id': ID, 'v1': V1, 'v2': V2}

    conn = db_connect()
    cur = conn.cursor()  # カーソルを取得

    cur.execute(sql, param)
    conn.commit()

    cur.close()  # カーソル クローズ
    db_connect_close(conn)

    return True


def db_data_del(id):
    sql = "DELETE TESTDATA WHERE ID = :1"
    param = (id)

    conn = db_connect()
    cur = conn.cursor()  # カーソルを取得

    cur.execute(sql, param)
    conn.commit()

    cur.close()  # カーソル クローズ
    db_connect_close(conn)

    return True
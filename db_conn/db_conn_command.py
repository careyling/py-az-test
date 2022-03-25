# load .env
from traceback import print_tb
import cx_Oracle

from dotenv import load_dotenv, find_dotenv
load_dotenv(verbose=True)

import os

TARGET_HOST = os.environ['TARGET_HOST']
PORT = os.environ['PORT']
SERVICE_NAME = os.environ['SERVICE_NAME']
USERNAME = os.environ['DBUSERNAME']
PASSWORD = os.environ['DBPASSWORD']

class OracleDatabase(object):
    """
    oracle
    """
    def __init__(self):
        """
        初期化
        """
        try:
            # tns = cx_Oracle.makedsn(TARGET_HOST, PORT, SERVICE_NAME)  # tnsを設定
            # conn = cx_Oracle.connect(USERNAME, PASSWORD, tns)  # DBに接続
            # tns = cx_Oracle.makedsn('dx.huangyi.cn','1521','ORCL')  # tnsを設定
            # conn = cx_Oracle.connect('C##VCC', 'VCC', tns)  # DBに接続
            # conn = cx_Oracle.connect('C##VCC', 'VCC', 'dx.huangyi.cn:1521/ORCL')
            self.connect = cx_Oracle.connect('C##VCC', 'VCC', 'dx.huangyi.cn:1521/ORCL')
            self.cursor = self.connect.cursor()
        except Exception as e:
            raise e

    def selectall(self, **kwargs):
        """
        データ検索
        """
        try:
            sql = 'sql' in kwargs and kwargs['sql'] or ''
            param = 'param' in kwargs and kwargs['param'] or ''
            self.cursor.execute(sql, param)
            return self.cursor.fetchall()
        except Exception as e:
            self.connect.rollback()
            print("データ検索エラー:{}".format(e))

    def selectone(self, **kwargs):
        """
        データ検索
        """
        try:
            sql = 'sql' in kwargs and kwargs['sql'] or ''
            param = 'param' in kwargs and kwargs['param'] or ''
            self.cursor.execute(sql, param)
            return self.cursor.fetchone()
        except Exception as e:
            self.connect.rollback()
            print("データ検索エラー:{}".format(e))

    def exec(self, **kwargs):
        """
        データ削除
        """
        try:
            sql = 'sql' in kwargs and kwargs['sql'] or ''
            param = 'param' in kwargs and kwargs['param'] or ''
            self.cursor.execute(sql, param)         
            self.connect.commit()
            row_count = self.cursor.rowcount
            return row_count
        except Exception as e:
            self.connect.rollback()
            print("データ操作エラー:{}".format(e))

    def __del__(self):
        """
        db接続をクローズ
        """
        self.cursor.close()
        self.connect.close()
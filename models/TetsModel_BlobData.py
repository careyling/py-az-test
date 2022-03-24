import sys,os
sys.path.append(os.getcwd())
from blob_conn import blob_conn_command

# load .env
from azure.storage.blob import BlockBlobService

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mycontainername = os.environ['CONTAINER_NAME']
myblobdic = os.environ['ENTRY_BLOB_DIC']

blob_conn = blob_conn_command.Blob()

def searchAll():
    try:
        datas = blob_conn.selectall(mycontainername,myblobdic)
        return datas
    except Exception as e:
        raise e


def searchOne(id):
    try:
        data = blob_conn.selectone(mycontainername,myblobdic+'/'+id)
        return data
    except Exception as e:
        raise e


def insert(data):
    try:
        evaldata = eval(data)
        id = evaldata['id']
        blob_name = myblobdic+'/'+id
        blob_conn.fix(mycontainername,blob_name,data)
        return True
    except Exception as e:
        raise e


def update(data):
    try:
        evaldata = eval(data)
        id = evaldata['id']
        blob_name = myblobdic+'/'+id
        blob_conn.fix(mycontainername,blob_name,data)
        return True
    except Exception as e:
        raise e


def delete(id):
    try:
        blob_name = myblobdic+'/'+id
        blob_conn.fix(mycontainername,blob_name)
        return True
    except Exception as e:
        raise e
import json
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

def searchAllValue():
    try:
        datas = blob_conn.selectall(mycontainername,myblobdic)
        vdatas =[]
        for data in datas:
            vdatas.append(getdatavalue(data))
        return vdatas
    except Exception as e:
        raise e


def searchOneValue(id):
    try:
        data = blob_conn.selectone(mycontainername,myblobdic+'/'+id)
        return getdatavalue(data)
    except Exception as e:
        raise e


def insert(data):
    try:
        id = str(data["ID"])
        blob_name = myblobdic+'/'+id
        blob_conn.fix(mycontainername,blob_name,data)
        return True
    except Exception as e:
        raise e


def update(data):
    try:
        id = str(data["ID"])
        blob_name = myblobdic+'/'+id
        blob_conn.fix(mycontainername,blob_name,data)
        return True
    except Exception as e:
        raise e


def delete(id):
    try:
        blob_name = myblobdic+'/'+id
        blob_conn.delete(mycontainername,blob_name)
        return True
    except Exception as e:
        raise e

def getdatavalue(data):
    id = str(data["ID"])
    v1 = str(data["V1"])
    v2 = str(data["V2"])
    return (id, v1, v2)
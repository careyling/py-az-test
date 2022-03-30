import json
import sys,os
sys.path.append(os.getcwd())
from blob_conn import blob_conn_command

# load .env
from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mycontainername = os.environ['CONTAINER_NAME']
myblobdic = os.environ['ENTRY_BLOB_DIC']

blob_conn = blob_conn_command.Blob(mycontainername)

def searchAll():
    try:
        blobs = blob_conn.selectall(myblobdic)
        datas =[]
        for blob in blobs:
            blobname = blob.name
            blob_client = blob_conn.container_client.get_blob_client(blobname)
            blobstr = blob_client.download_blob().readall().decode('utf-8') # read blob content as string
            dictdata = json.loads(blobstr)
            datas.append(getdatavalue(dictdata))
        return datas
    except Exception as e:
        raise e


def searchOne(id):
    try:
        blobstr = blob_conn.selectvalue(myblobdic+'/'+id)
        dictdata = json.loads(blobstr)
        return getdatavalue(dictdata)
    except Exception as e:
        raise e


def insert(data):
    try:
        id = str(data["ID"])
        blob_name = myblobdic+'/'+id
        blob_conn.insert(blob_name,json.dumps(data))
        return True
    except Exception as e:
        raise e


def update(data):
    try:
        id = str(data["ID"])
        blob_name = myblobdic+'/'+id
        blob_conn.update(blob_name,json.dumps(data))
        return True
    except Exception as e:
        raise e


def delete(id):
    try:
        blob_name = myblobdic+'/'+id
        blob_conn.delete(blob_name)
        return True
    except Exception as e:
        raise e


def getdatavalue(data):

    id = str(data["ID"])
    v1 = str(data["V1"])
    v2 = str(data["V2"])
    return (id, v1, v2)
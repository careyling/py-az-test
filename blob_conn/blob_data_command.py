# load .env
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import os,json

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mystoragename = os.environ['BLOB_STORGENAME']
mystoragekey = os.environ['BLOB_STORGEKEY']
mycontainername = os.environ['CONTAINER_NAME']
myblobdic = os.environ['CONTAINER_BLOB_DIC']

blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)

def db_data_selectall():
    try:
        blobs = blob_service.list_blobs(mycontainername)
        datas = []
        for blob in blobs:
            blobstr = blob_service.get_blob_to_text(mycontainername,blob.name).content
            evaldata = eval(blobstr)
            id = evaldata['id']
            v1 = evaldata['v1']
            v2 = evaldata['v2']
            tuplestr = (id,v1,v2)
            datas.append(tuplestr)
        return datas
    except Exception as e:
        raise e


def db_data_selectone(id):
    try:
        blob_name = myblobdic+'/'+id
        blobstr = blobstr = blob_service.get_blob_to_text(mycontainername,blob_name).content
        evaldata = eval(blobstr)
        id = evaldata['id']
        v1 = evaldata['v1']
        v2 = evaldata['v2']
        tuplestr = (id,v1,v2)
        return tuplestr
    except Exception as e:
        raise e


def db_data_add(data):
    try:
        evaldata = eval(data)
        id = evaldata['id']
        blob_name = myblobdic+'/'+id
        blob_service.create_blob_from_text(
            container_name=mycontainername,
            blob_name=blob_name,
            text=data)
        return True
    except Exception as e:
        raise e

def db_data_upd(data):
    try:
        evaldata = eval(data)
        id = evaldata['id']
        blob_name = myblobdic+'/'+id
        blob_service.create_blob_from_text(
            container_name=mycontainername,
            blob_name=blob_name,
            text=data)
        return True
    except Exception as e:
        raise e


def db_data_del(id):
    try:        
        blob_name = myblobdic+'/'+id
        blob_service.delete_blob(mycontainername, blob_name)
        return True
    except Exception as e:
        raise e
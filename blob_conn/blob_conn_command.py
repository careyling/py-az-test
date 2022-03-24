# load .env
from azure.storage.blob import BlockBlobService
import os,json

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mystoragename = os.environ['BLOB_STORGENAME']
mystoragekey = os.environ['BLOB_STORGEKEY']
# mycontainername = os.environ['CONTAINER_NAME']
# myblobdic = os.environ['ENTRY_BLOB_DIC']

blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)

def data_selectall(containername,blobdic):
    try:
        blobs = blob_service.list_blobs(containername)
        datas = []
        for blob in blobs:
            blobname = blob.name
            if blobname.startswith(blobdic):
                blobstr = blob_service.get_blob_to_text(containername,blobname).content
                evaldata = eval(blobstr)                
                datas.append(evaldata)
        return datas
    except Exception as e:
        raise e

def data_selectone(containername,blobname):
    try:
        blobstr = blobstr = blob_service.get_blob_to_text(containername,blobname).content
        evaldata = eval(blobstr)
        return evaldata
    except Exception as e:
        raise e

#data:'{"id": "1", "v1": "2", "v2": "3"}'
def data_fix(containername,blobname,data):
    try:
        blob_service.create_blob_from_text(
            container_name=containername,
            blob_name=blobname,
            text=data)
        return True
    except Exception as e:
        raise e

def db_data_del(containername,blobname):
    try:
        blob_service.delete_blob(containername, blobname)
        return True
    except Exception as e:
        raise e
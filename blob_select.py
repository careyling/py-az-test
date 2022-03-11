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
blobs = blob_service.list_blobs(mycontainername)
datas = []
for blob in blobs:
    blobstr = str(blob_service.get_blob_to_text(mycontainername,blob.name).content)
    evaldata = eval(blobstr)
    id = evaldata['id']
    v1 = evaldata['v1']
    v2 = evaldata['v2']
    tuplestr = (id,v1,v2)
    datas.append(tuplestr)
print (datas)
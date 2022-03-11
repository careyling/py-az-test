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

data = '{"id": "1", "v1": "2", "v2": "3"}'

evaldata = eval(data)

id = evaldata['id']
blob_name = myblobdic+'/'+id
tt = blob_service.create_blob_from_text(
    container_name=mycontainername,
    blob_name=blob_name,
    text=str(data))

print (type(tt))
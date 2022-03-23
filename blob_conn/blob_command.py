# load .env
from azure.storage.blob import BlockBlobService
import os,json

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mystoragename = os.environ['BLOB_STORGENAME']
mystoragekey = os.environ['BLOB_STORGEKEY']
mycontainername = os.environ['CONTAINER_NAME']
entryblobdic = os.environ['ENTRY_BLOB_DIC']
resultblobdic = os.environ['RESULT_BLOB_DIC']

blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)

#同BLOB
def downloadFilesInContainer():
    try:
        blobs = blob_service.list_blobs(mycontainername)
        for blob in blobs:
            entryblobname = blob.name
            if entryblobname.startswith(entryblobdic):
                resultblobname = entryblobname.replace(entryblobdic, resultblobdic)
                blob_url = blob_service.make_blob_url(mycontainername, entryblobname)
                blob_service.copy_blob(mycontainername,resultblobname,blob_url)
    except Exception as e:
        raise e

#同BLOB
def moveFilesInContainer():
    try:
        blobs = blob_service.list_blobs(mycontainername)
        for blob in blobs:
            entryblobname = blob.name
            if entryblobname.startswith(entryblobdic):
                resultblobname = entryblobname.replace(entryblobdic, resultblobdic)
                blob_url = blob_service.make_blob_url(mycontainername, entryblobname)
                blob_service.copy_blob(mycontainername,resultblobname,blob_url)
                #delete
                blob_service.delete_blob(mycontainername, entryblobname)
    except Exception as e:
        raise e

moveFilesInContainer()
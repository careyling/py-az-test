# load .env
from azure.storage.blob import BlockBlobService
import os,json

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

mystoragename = os.environ['BLOB_STORGENAME']
mystoragekey = os.environ['BLOB_STORGEKEY']
# mycontainername = os.environ['CONTAINER_NAME']
# myblobdic = os.environ['ENTRY_BLOB_DIC']

class Blob(object):
    """
    blob
    """
    def __init__(self):
        """
        初期化
        """
        try:
            self.blob_service = BlockBlobService(account_name=mystoragename, account_key=mystoragekey)
        except Exception as e:
            raise e

    def selectall(self,containername,blobdic):
        try:
            blobs = self.blob_service.list_blobs(containername)
            datas = []
            for blob in blobs:
                blobname = blob.name
                if blobname.startswith(blobdic):
                    blobstr = self.blob_service.get_blob_to_text(containername,blobname).content
                    evaldata = eval(blobstr)                
                    datas.append(evaldata)
            return datas
        except Exception as e:
            print("データ検索エラー:{}".format(e))

    def selectone(self,containername,blobname):
        try:
            blobstr = self.blob_service.get_blob_to_text(containername,blobname).content
            evaldata = eval(blobstr)
            return evaldata
        except Exception as e:
            print("データ検索エラー:{}".format(e))

    #data:'{"id": "1", "v1": "2", "v2": "3"}'
    def fix(self,containername,blobname,data):
        try:
            self.blob_service.create_blob_from_text(
                container_name=containername,
                blob_name=blobname,
                text=str(data))
            return True
        except Exception as e:
            print("データ操作エラー:{}".format(e))

    def delete(self,containername,blobname):
        try:
            self.blob_service.delete_blob(containername, blobname)
            return True
        except Exception as e:
            raise e
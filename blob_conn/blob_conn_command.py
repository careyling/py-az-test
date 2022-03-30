# load .env
from azure.storage.blob import BlobServiceClient
import os,json

from dotenv import load_dotenv,find_dotenv
load_dotenv(verbose=True)

myconnect_str = os.environ['CONNECT_STR']

class Blob(object):
    """
    blob
    """
    def __init__(self,containername):
        """
        初期化
        """
        try:
            self.blob_service_client = BlobServiceClient.from_connection_string(myconnect_str)
            self.container_client = self.blob_service_client.get_container_client(containername)
        except Exception as e:
            raise e

    def selectall(self,blobdic):
        try:
            blobs = self.container_client.list_blobs(name_starts_with=blobdic)
            return blobs
        except Exception as e:
            print("データ検索エラー:{}".format(e))

    def selectvalue(self,blobname):
        try:
            blob_client = self.container_client.get_blob_client(blobname)            
            blobstr = blob_client.download_blob().readall().decode('utf-8') # read blob content as string
            return blobstr
        except Exception as e:
            print("データ検索エラー:{}".format(e))

    #data:'{"id": "1", "v1": "2", "v2": "3"}'
    def insert(self,blobname,data):
        try:
            blob_client = self.container_client.get_blob_client(blobname)
            metadata = dict(type="testdata")
            blob_client.upload_blob(data,metadata=metadata)
        except Exception as e:
            print("データ操作エラー:{}".format(e))


    #data:'{"id": "1", "v1": "2", "v2": "3"}'
    def update(self,blobname,data):
        try:
            blob_client = self.container_client.get_blob_client(blobname)
            metadata = dict(type="testdata")
            blob_client.delete_blob()
            blob_client.upload_blob(data,metadata=metadata)
        except Exception as e:
            print("データ操作エラー:{}".format(e))


    def delete(self,blobname):
        try:
            
            blob_client = self.container_client.get_blob_client(blobname)
            blob_client.delete_blob()
            return True
        except Exception as e:
            raise e
cd /d D:\PythonProjects\deploy-pyhton-on-azure\py-az-test
py -3 -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
set FLASK_APP=blobtest:myapp
flask run
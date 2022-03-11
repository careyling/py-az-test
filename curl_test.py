import pycurl
from io import BytesIO

url = 'www.baidu.com'

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
print(body.decode('iso-8859-1'))
import requests
import re,sys,io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')

url = 'http://www.204sihu.com'
res = requests.request('GET',url).encoding('utf-8')
#res.encoding= 'utf-8'
print(res.text)
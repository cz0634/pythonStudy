from urllib import request, parse
import json
import time
import random

url = 'http://2000019.ip138.com'
iplist = ['182.34.33.163:9999', '182.34.33.163:9999', '182.34.33.163:9999']

proxy_support = request.ProxyHandler({'https':random.choice(iplist)})
opener = request.build_opener(proxy_support)

opener.addheaders = [{'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}]

request.install_opener(opener)
response = request.urlopen(url)
html = response.read().decode('utf-8')
#html = response.read()
print(html)
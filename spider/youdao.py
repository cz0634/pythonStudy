from urllib import request, parse
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {}
data['i'] = 'cz very cool'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15714520957487'
data['sign'] = '11655fb149123e49b238cd2f2615ddb0'
data['ts'] = '1571452095748'
data['bv'] = '0e5478153d48e38fe749c1641f896916'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data = parse.urlencode(data).encode('utf-8')

response = request.urlopen(url, data)
html = response.read().decode('utf-8')

print(html)
target = json.loads(html)
print(type(html))
print(type(target))
print(target)
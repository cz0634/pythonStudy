from urllib import request, parse
import json
import time

while True:
    content = input('输入"q!"退出程序')
    if content == 'q!':
        print('程序退出。')
        break;

    url = 'https://novel.mkread.com/Admin/Login/checkLogin.html'

    data = {}
    data['username'] = 'admin'
    data['password'] = 'asdasd'
    data = parse.urlencode(data)

    #request对象
    req = request.Request(url)
    #添加请求头部
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    with request.urlopen(req, data.encode('utf-8')) as f:
        res = f.read()
        res = res.decode('utf-8')
        print(res)
    time.sleep(5) #休息5秒


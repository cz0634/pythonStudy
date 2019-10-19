from urllib import request

def getHtml(url):
    response = request.urlopen(url)
    return response.read()

def saveHtml(path, content):
    htmlFile = open(path, 'w')
    htmlFile.write(content)
    htmlFile.close()

checkurl = input('请输入要检测的域名：')
if len(checkurl) <= 0:
    print('域名不能为空')
    exit()

url = 'https://mp.weixinbridge.com/mp/wapredirect?url=' + checkurl
html = getHtml(url)
html = html.decode('utf-8')

if len(html) <= 0:
    print('检测内容有误')
elif html.find('var cgiData = {') >= 0:
    print('域名已被封')
else:
    print('域名正常')
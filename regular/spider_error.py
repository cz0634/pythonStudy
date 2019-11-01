from urllib import request,parse,error

req = request.Request('http://www.aaaaaaaaaaaaaaooxx-fishc.com')
try:
    request.urlopen(req)
except error.URLError as e:
    if hasattr(e, 'reason'):
        print('reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('Error code: ', e.code)
    else:
        ''
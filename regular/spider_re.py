from urllib import request, parse
import re

def getHtml(url):
    res = request.Request(url)
    res.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    with request.urlopen(res) as f:
        html = f.read().decode('utf-8')
    return html

def getIps(url):
    html = getHtml(url)
    ips = re.findall(r'<td>((?:\d{1,3}\.){3}\d{1,3})</td>', html)  #?:非捕获组
    ports = re.findall(r'<td>(\d+)</td>', html)
    prefix = re.findall(r'<td>(HTTP|HTTPS)</td>', html)

    ipList = []
    for index in range(0, len(ips)-1):
        ipList.append(prefix[index].lower() + '-' + ips[index] + ':' + str(ports[index]) )

    print(ipList)

if __name__ == '__main__':
    url = 'https://www.xicidaili.com/wt/'
    getIps(url)



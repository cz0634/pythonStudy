from urllib import request, parse
import os
import base64

def url_open(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    response = request.urlopen(req)
    return  response.read()


def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src=', b)

    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        with open(each.split('/')[-1], 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)


def download_mm(folder='img', pages=10):
    os.mkdir(folder)
    os.chdir(folder) #改变目录

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        page_str = '20191021-' + str(page_num)
        page_str = str(base64.b64encode(page_str.encode('utf-8')),'utf-8')
        page_url = url + page_str + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()

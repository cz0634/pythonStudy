from urllib import request

response = request.urlopen('http://placekitten.com/g/200/300')
cat_img = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_img)

print(response.geturl()) #访问的url
print(response.info())   #header信息
print(response.getcode())#返回状态码

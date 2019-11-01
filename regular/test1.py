import re

print(re.search('.', 'cz cool'))        #.匹配换行符以外的所有字符
print(re.search(r'\d', 'aaa123123'))    #\d匹配数字
print(re.search(r'[aeiouAEIOU]', 'I love aaa')) #匹配中括号里面的字符
print(re.search(r'[0-9]', 'I 123 love aaa'))    #匹配中括号里面的字符
print(re.search(r'ab{3}c', 'aaa abbbc'))        #{}指定匹配次数
print(re.search(r'ab{3,10}c', 'aaa abbbc'))        #{}指定匹配次数

#正则匹配0-255
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '249'))
#正则匹配ip
print(re.search(r'(([01]{0,1}\d{0,1}\d{0,1}|2{0,1}[0-4]{0,1}\d{0,1}|2{0,1}5{0,1}[0-5]{0,1})\.){3}([01]{0,1}\d{0,1}\d{0,1}|2{0,1}[0-4]{0,1}\d{0,1}|2{0,1}5{0,1}[0-5]{0,1})', '47.92.127.55'))
import re

print(re.findall(r'[a-z]', "cz cool"))
print(re.findall(r'[^a-z]', "cz cool")) #除了a-z其他都匹配

s = "<html><title>cz cool</title></html>"
print(re.search(r'<.+>', s))  #贪婪匹配
print(re.search(r'<title>.+</title>', s))  #贪婪匹配
#print()
result = re.search(r'<.+?>', s) #非贪婪匹配
print(result.group())
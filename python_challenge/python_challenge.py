# Challenge 0
print( 2 ** 38)

# Challenge 1
data = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

print(''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in data]))

translation = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
result = 'map'.translate(translation)
print(result)

# Challenge 2
import urllib.request
import re
url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().decode()
data = re.findall('<!--(.*?)-->', url, re.DOTALL)[-1]
print(''.join(re.findall('[A-Za-z]', data)))

# Challenge 3
# import necessary packages as above challenge
url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode()
data = re.findall('<!--(.*?)-->', url, re.DOTALL)[-1]
print(''.join(re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', data)))


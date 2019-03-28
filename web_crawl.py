from bs4 import BeautifulSoup

myHTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试爬虫用的网站</title>
</head>
<body>
    <h1>大标题</h1>
    <h2>小标题1</h2>
    <h2>小标题2</h2>
    <p>一段文字</p>
</body>
</html>'''

my_parser = BeautifulSoup(myHTML,'html.parser')

#myH1 = my_parser.find('h1')

#print(myH1)

#print(myH1.string)

find_h2 = my_parser.findAll('h2')

print(find_h2)

for i in find_h2:
    if '1' in i.string:
        print(i.string)
from bs4 import BeautifulSoup
import requests

#获取网站内容1，url
google = requests.get("http://www.google.com").content
#print(google)

#baidu = requests.get('http://www.baidu.com').content

#对网站内容解析 1 内容 2 html.paser
soup1 = BeautifulSoup(google,'html.parser')
#soup2 = BeautifulSoup(baidu,'html.parser')

#内容爬取文字
#print(soup2.text)

#寻找特定内容
links = soup1.findAll('a')

print(links)
'''
for i in links:
    print(i)
'''

#标题
#print(soup2.title.string)
'''
horn = requests.get('http://www.vias.org/crowhurstba/crowhurst_basic_audio_vol1_049.html').content
physic = BeautifulSoup(horn,'html.parser')
text = physic.findAll('p')
print(physic.text)
'''
#获取网页的大小
#google = requests.get("http://www.google.com")
#print(google.status_code)

#获取网页标题
#print(google.headers)

#parser:语法分析（英语：syntactic analysis，也叫 parsing）
# 是根据某种给定的形式文法对由单词序列（如英语单词序列）
# 构成的输入文本进行分析并确定其语法结构的一种过程。

#src = requests.get("http://www.baidu.com").content
#xml = BeautifulSoup(src,'lxml')#需要安装C语言库
#soup = BeautifulSoup(src,'html.parser')
#print(soup)

#找出所有的连接
#html中连接用a标签
#links = soup.find_all('a')
#print(links)

'''
#使用for循环将所有的连接遍历一遍
#寻找链接中含有百度字符的，
for link in links:
    if '百度' in link.text:
        print(link)
        print(link.attrs['href'])#打印纯链接

'''
#打印完整的html格式
#print(soup.prettify())
'''
#打印加粗的内容
print(soup.b)
print(soup.find('b'))
print(soup.find_all('b'))#返回一个列表
#带有b标签的标签名字
print(soup.b.name)

fuck = soup.b
fuck.name = 'fuck'

print(fuck)
'''
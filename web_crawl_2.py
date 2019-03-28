from bs4 import BeautifulSoup
import requests

#获取网站内容1，url
#google = requests.get("http://www.google.com").content
#print(google)

#baidu = requests.get('http://www.baidu.com').content

#对网站内容解析 1 内容 2 html.paser
#soup1 = BeautifulSoup(google,'html.parser')
#soup2 = BeautifulSoup(baidu,'html.parser')

#内容爬取文字
#print(soup2.text)

#寻找特定内容
#links = soup2.findAll('a')

#print(links)
'''
for i in links:
    print(i)
'''

#print(soup2.title.string)

horn = requests.get('http://www.vias.org/crowhurstba/crowhurst_basic_audio_vol1_049.html').content
physic = BeautifulSoup(horn,'html.parser')
text = physic.findAll('p')
print(physic.text)
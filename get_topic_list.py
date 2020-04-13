from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, csv, os


html = urlopen(
    "https://s.weibo.com/top/summary?cate=realtimehot"
).read().decode('utf-8')

# print(html,file= open('a.html', 'w'))
# html = open('./a.html').read()

soup = BeautifulSoup(html, features='lxml')
td_list = soup.find_all("td", {'class': 'td-02'}) # 热搜列表有效部分

# print(td_list.a)

topic_list = []


headers = ('Title', 'Link', 'Trending Count', 'Emotion')

with open('./2020-04-13.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(headers)
    for td in td_list:
        if td.span: trending_count = td.span.string 
        else: trending_count = None
        if td.img: emotion = td.img['alt'] 
        else: emotion = None
        row = (td.a.string, td.a['href'], trending_count, emotion)
        writer.writerow(row)


# html = open('./a.html').read()
# soup = BeautifulSoup(html, features='lxml')


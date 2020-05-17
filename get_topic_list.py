from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, csv, os, datetime


html = urlopen("https://s.weibo.com/top/summary?cate=realtimehot").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
td_list = soup.find_all('td', {'class': 'td-02'}) # 热搜列表有效部分

topic_list = []

date = datetime.date.today().strftime('%Y-%m-%d')
if not os.path.exists('./data/' + date):
    os.mkdir('./data/' + date)

headers = ('Title', 'Trending Count', 'Emotion')

with open('./data/' + date + '.csv', 'a', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(headers)
    for td in td_list:
        if td.a['href'] == 'javascript:void(0);': # 排除广告
            continue
        if td.span: trending_count = td.span.string 
        else: trending_count = None
        if td.img: emotion = td.img['alt'] 
        else: emotion = None
        row = (td.a.string, trending_count, emotion)
        writer.writerow(row)

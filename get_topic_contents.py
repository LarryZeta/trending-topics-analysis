from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, csv, os, datetime

def get_topic_contents(name, uri, date):
    html = urlopen('https://s.weibo.com' + uri).read().decode('utf-8')

    # f = open('a.html', 'w')
    # print(html, file=f)

    # f = open('a.html', 'r')
    # html = f.read()

    soup = BeautifulSoup(html, features='lxml')
    feeds = soup('div', {'action-type': 'feed_list_item'})

    file_name = './data/'+ date + '/' + name + '.csv'

    headers = ('name', 'text')
    with open(file_name, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(headers)
        for feed in feeds:
            name = feed.find('a', {'class': 'name'}).string  # 微博昵称
            text = feed.find('p', {'class': 'txt', 'node-type': "feed_list_content_full"}) # 微博正文
            if text is not None: 
                text = text.get_text().replace(' ','').replace('\n', '')
            else: 
                text = feed.find('p', {'class': 'txt', 'node-type': "feed_list_content"}).get_text().replace(' ','').replace('\n', '')
            row = (name, text)
            writer.writerow(row)

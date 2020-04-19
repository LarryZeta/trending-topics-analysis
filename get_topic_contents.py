from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
import re, csv, os, datetime, requests, random

def get_topic_contents(topic_name, date):
    
    cookie_str = ''
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.strip().split('=', 1)
        cookies[key] = value
    
    r = requests.get('https://s.weibo.com/weibo', {'q': topic_name}, cookies = cookies)
    html = r.content.decode('utf-8')
    # html = urlopen('https://s.weibo.com' + uri).read().decode('utf-8')

    # f = open('a.html', 'w')
    # print(html, file=f)

    # f = open('a.html', 'r')
    # html = f.read()
    soup = BeautifulSoup(html, features='lxml')
    li = soup.find('ul', {'class': 's-scroll'})('li')
    pages_num = len(li) # 热搜页数

    file_name = './data/'+ date + '/' + topic_name + '.csv'
    headers = ('user_name', 'text')
    page = 1
    sleep_page = 1
    qbar = tqdm(total=pages_num)

    with open(file_name, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(headers)
    
        while True:
            feeds = soup('div', {'action-type': 'feed_list_item'})

            for feed in feeds:
                user_name = feed.find('a', {'class': 'name'}).string  # 微博昵称
                text = feed.find('p', {'class': 'txt', 'node-type': "feed_list_content_full"}) # 微博正文
                if text is not None: 
                    text = text.get_text().replace(' ','').replace('\n', '')
                else: 
                    text = feed.find('p', {'class': 'txt', 'node-type': "feed_list_content"}).get_text().replace(' ','').replace('\n', '')
                row = (user_name, text)
                writer.writerow(row)
            
            page = page + 1
            qbar.update(1)

            if page <= pages_num:
                if page == sleep_page:
                    sleep(random.randint(6, 10))
                    sleep_page = sleep_page + random.randint(1, 5)
                r = requests.get('https://s.weibo.com/weibo', {'q': topic_name, 'page': page}, cookies = cookies) # 发送下一页请求
                html = r.content.decode('utf-8')
                soup = BeautifulSoup(html, features='lxml')
                
                sleep(random.randint(1, 3))
            else:
                qbar.close()
                break
    
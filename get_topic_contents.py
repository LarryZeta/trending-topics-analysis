from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, csv, os


# html = urlopen(
#     "https://s.weibo.com/weibo?q=%23%E6%A2%B5%E9%AB%98%E6%98%9F%E7%A9%BA%E5%90%90%E5%8F%B8%23&Refer=top"
# ).read().decode('utf-8')
f = open('a.html', 'r')
html = f.read()

soup = BeautifulSoup(html, features='lxml')
card_wraps = soup.findAll('div', {'class': 'card-wrap'})

print(card_wraps[1].find('a', {'class': 'name'}).string) # 微博昵称
print(card_wraps[1].find('p', {'class': 'txt'}).get_text()) # 微博正文
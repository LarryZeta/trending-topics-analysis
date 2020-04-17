import re, csv, os, datetime, requests
from bs4 import BeautifulSoup

cookie_str = 'UOR=bbs.aptx.cn,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=7013905332748.457.1584003865013; ULV=1584003866020:1:1:1:7013905332748.457.1584003865013:; SCF=ApvXF8YzDLgwWPzUMd2sb_6uPp2HV_-L96IROT0H59hWqsLHFREeEcvSUoMO1fJF-B6VTlKtQGM5tpo3i42q1Sc.; SUHB=09P9U-HbOjVaRz; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFW-LvpH4oXIzuP4wUT1fvR5JpX5K2hUgL.Fo-X1hnceKeRSoM2dJLoI7LeqPiEwHDLUs2t; ALF=1618591793; un=18810817370; wvr=6; webim_unReadCount=%7B%22time%22%3A1587057455939%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; _s_tentry=bbs.aptx.cn; Apache=7013905332748.457.1584003865013; login_sid_t=053dff415dda6dbc469f0df0de88c3fc; cross_origin_proto=SSL; SUB=_2A25znPziDeRhGeNK41oX8S3EzTuIHXVQ6GkqrDV8PUNbmtAKLUHWkW9NSVUNPnbhCiakR2iWcL1r7_3Z56cADAsy; SSOLoginState=1587055794; WBStorage=42212210b087ca50|undefined'
cookies = {}
for line in cookie_str.split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value

r = requests.get("https://s.weibo.com/weibo?q=%23%E4%BA%95%E6%9F%8F%E7%84%B6%E5%92%8C%E6%9D%8E%E4%BD%B3%E7%90%A6%E8%AE%A8%E8%AE%BA%E6%90%93%E6%BE%A1%23&Refer=top", cookies = cookies)

html = r.content.decode('utf-8')

# f = open('a.html', 'w')
# print (r.content.decode('utf-8'), file=f)

# f = open('a.html', 'r')
# html = f.read()

soup = BeautifulSoup(html, features='lxml')
li = soup.find('ul', {'class': 's-scroll'})('li')
pages_num = len(li) # 热搜页数

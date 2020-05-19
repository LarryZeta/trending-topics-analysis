import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
import yaml
import csv
from time import sleep

# 接口地址
url = "https://ltpapi.xfyun.cn/v2/sa"


with open('./config.yml', 'r') as config_file:
    config = yaml.load(config_file.read(), Loader=yaml.SafeLoader)
    x_appid = config['xf_appid']
    api_key = config['xf_api_key']

def analysis(TEXT):
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    return result.decode('utf-8')




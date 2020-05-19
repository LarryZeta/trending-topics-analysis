import yaml, json, csv
import time
import urllib.request
import urllib.parse
import hashlib
import base64
import sys
from time import sleep


def get_all_weibos():
    
    weibos = []
    weibo_csv = open('./data/weibos.csv', 'r')
    weibo_reader = csv.reader(weibo_csv)
    
    for line in weibo_reader:
        if weibo_reader.line_num == 1:
            continue
        weibo = (line[0], line[1], line[2])
        weibos.append(weibo)
    
    return weibos


def get_emotion(TEXT, x_appid, api_key):
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
    res_json = result.decode('utf-8')
    print(res_json)
    return res_json


if __name__ == '__main__':
    weibos = get_all_weibos()

    url = 'https://ltpapi.xfyun.cn/v2/sa'
    with open('./config.yml', 'r') as config_file:
        config = yaml.load(config_file.read(), Loader=yaml.SafeLoader)
    
    csv_file_name = './data/weibos_res_'+ sys.argv[1] + '_'+ sys.argv[2] +'.csv'
    res_csv = open(csv_file_name, 'a', newline='')
    res_writer = csv.writer(res_csv)
    # length = 8752
    # index = 31249 - 2 # 第 index 条开始 数值为：行数 - 2
    length = int(sys.argv[2])
    index = int(sys.argv[1]) - 2
    for i in range(index, index + length):
        weibo = weibos[i]
        res_json_str = get_emotion(
            weibo[2][:160],
            config['xf_appid'], 
            config['xf_api_key'],
            )
        res_json = json.loads(res_json_str)
        
        if res_json['data']:
            sentiment_num = res_json['data']['sentiment']
            sentiment_value = res_json['data']['score']
        else:
            sentiment_num = None
            sentiment_value = None
            with open('./data/error', 'a') as error_file:
                error_file.write('error:' + str(i))
        res = (weibo[0], weibo[1], weibo[2], res_json_str, sentiment_num, sentiment_value)
        res_writer.writerow(res)
        sleep(0.5)

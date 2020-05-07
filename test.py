#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
#接口地址
url ="https://ltpapi.xfyun.cn/v2/sa"
#开放平台应用ID
x_appid = "5eb3d844"
#开放平台应用接口秘钥
api_key = "c612ae517fad0bffd3f6230e13616895"
#语言文本
TEXT="半吊子的人才是最痛苦的。上进的心维持两天就熄灭，堕落却不敢放肆堕落，常常感到自卑，也常常忍不住膨胀。乐观吧，又时不时丧一下，悲观吧，又偶尔踌躇满志。这也好那也行，犹犹豫豫做不了选择，整个人处于极其拧巴的状态，在纠结和反复中不停蹉跎。#很努力但成绩差是什么体验#​"


def main():
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
    print(result.decode('utf-8'))
    return


if __name__ == '__main__':
    main()

import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
import yaml

with open('./config.yml', 'r') as config_file:
    config = yaml.load(config_file.read(), Loader=yaml.SafeLoader)
    x_appid = config['xf_appid']
    api_key = config['xf_api_key']
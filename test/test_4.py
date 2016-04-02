#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import request
import json
from pprint import pprint
from collections import OrderedDict

req = request.Request('http://new.36kr.com/newsflashes.json')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    if(200 == f.status):
        data = f.read()
        with open('test_4.json', 'w') as f_36kr:
            f_36kr.write(data.decode('utf-8'))
            f_36kr.close()
        json_data = json.loads(data.decode('utf-8'), object_pairs_hook=OrderedDict)
    else:
        print('Status Error!\n')

temp = json_data["data"]['newsflashes']
for i in range(2):
    print(temp[i]['hash_title']+'\n')

print('done!\n')

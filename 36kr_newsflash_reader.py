#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request, error
import json

req = request.Request('http://new.36kr.com/newsflashes.json')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')

try:
	resp = request.urlopen(req)
	print('Status:', resp.status, resp.reason + '\n')
	if 200 == resp.status:
		data = resp.read().decode('utf-8')
		json_data = json.loads(data)
		for i in range(10):
			print(json_data["props"]["newsflashList|newsflash"][i]['title']+'\n')
except error.HTTPError as e:
	# in case of 404
	print(e)
print('Done!\n')

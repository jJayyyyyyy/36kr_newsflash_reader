#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import json

first_page_url = 'http://36kr.com/api/newsflash'

def get_json_data(url=first_page_url):
	req = request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
	resp = request.urlopen(req)
	print('Status:', resp.status, resp.reason + '\n')
	if(200 == resp.status):
		data = resp.read().decode('utf-8', 'ignore')
		return json.loads(data)
	else:
		print('Status Error!\n')
		exit(0)

def get_news(json_data):
	while True:
		for news in json_data['data']['items']:
			us_input = input('\n' + news['title'])
			if 'q' == us_input:
				print('\nDone!\n')
				return 1
			elif 'd' == us_input:
				print(news['updated_at'] + '\n' + news['description'] + '\n\n')
			else:
				pass
			news_id = news['id']

		print('\n--------- Next Page ---------')
		new_page_url = first_page_url + '?b_id=' + str(news_id) + '&d=mext'
		json_data = get_json_data(new_page_url)


get_news(get_json_data())


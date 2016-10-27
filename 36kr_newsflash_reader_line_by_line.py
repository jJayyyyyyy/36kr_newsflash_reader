#!/usr/bin/python3
# -*- coding: utf-8 -*-
from urllib import request
import json

first_page = 'http://36kr.com/api/newsflash'

def get_news(url=first_page):
	req = request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
	with request.urlopen(req) as f:
		print('Status:', f.status, f.reason + '\n')
		if(200 == f.status):
			data = f.read()
			json_data = json.loads(data.decode('utf-8', 'ignore'))
			return json_data
		else:
			print('Status Error\n')
			return 'Status Error'

def print_news(json_data):
	while True:
		for i in json_data['data']['items']:
			s = input('\n' + i['title'])
			if s == 'q':
				print('\nDone\n')
				return 1
			elif s == 'd':
				print(i['updated_at'] + '\n' + i['description'] + '\n\n\n')
			news_id = i['id']

		print('\n--------- Next Page ---------')
		new_page_url = first_page + '?b_id=' + str(news_id) + '&d=mext'
		json_data = get_news(new_page_url)


json_data = get_news()
print_news(json_data)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import request
import json

global news_id
news_id = 0

req = request.Request('http://new.36kr.com/newsflashes.json')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')


def get_news(req):
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason + '\n')
        if(200 == f.status):
            data = f.read()
            json_data = json.loads(data.decode('utf-8'))
        else:
            print('Status Error!\n')

    titles = json_data["data"]['newsflashes']
    for news_title in titles:
        global news_id
        news_id = news_title['id']
        print(news_id)
        print(news_title['hash_title']+'\n')

get_news(req)

# there are 30 titles every page
# when click 'see more' you can get another 30 titles which is earlier published
# and we can find the url-format is something lik:
# 'http://new.36kr.com/newsflashes.json?b_id=17951&d=next',
# and that is 'http://new.36kr.com/newsflashes.json?b_id=' + str(news_id) + '&d=next'

new_url = 'http://new.36kr.com/newsflashes.json?b_id=' + str(news_id) + '&d=next'
print(new_url)
req = request.Request(new_url)

get_news(req)

print('done!\n')

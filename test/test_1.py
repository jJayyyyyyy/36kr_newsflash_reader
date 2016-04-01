#!/usr/bin/python3
# -*- coding: utf-8 -*-
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
# 例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取， 并返回响应：

from urllib import request

req = 'https://api.douban.com/v2/book/2129650'

with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：

from urllib import request

req = request.Request('https://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')


with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    #print('Data:', data.decode('utf-8'))
    with open('./mobile_douban.html', 'w') as fdouban:
        # 'w' --> str, 'wb' --> 二进制文件
        # when 'wb', no need to decode data
        fdouban.write(data.decode('utf-8'))
        fdouban.close()

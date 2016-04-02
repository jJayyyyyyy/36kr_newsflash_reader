#!/usr/bin/python3
# -*- coding: utf-8 -*-
# There are bugs.

from urllib import request
from bs4 import BeautifulSoup

req = request.Request('http://new.36kr.com/newsflashes')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    if(200 == f.status):
        data = f.read()
        with open('test_3.html', 'w') as f_36kr:
            f_36kr.write(data.decode('utf-8'))
            f_36kr.close()
    else:
        print('Status Error!\n')

data = {}
soup = BeautifulSoup(open('test_3.html'), 'html.parser', from_encoding='utf-8')
title = soup.find("p", class_="story").find('a', id='link3')
data["title"] = title.get_text()


fout = open('out.html', 'w')
fout.write('<html>')
fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>')
fout.write('<body>')
fout.write('<table>')
fout.write('<tr>')
fout.write('<td>%s</td>' % data["title"])
fout.write('</tr>')
fout.write('</table>')
fout.write('<body>')
fout.write('<html>')
fout.close()



print('done!\n')

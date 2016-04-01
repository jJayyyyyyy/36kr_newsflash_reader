#!/usr/bin/python3
# -*- coding: utf-8 -*-

data = '测试'

fout = open('out.html', 'w')
fout.write('<html>')
fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>')
fout.write('<body>')
fout.write('<table>')

fout.write('<tr>')
fout.write('<td>%s</td>' % data)
fout.write('</tr>')

fout.write('</table>')
fout.write('<body>')
fout.write('<html>')
fout.close()

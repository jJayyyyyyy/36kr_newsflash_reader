#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4_test.html'), 'html.parser')

title = soup.find("p", class_="story").find('a', id='link3')
print(title.get_text())

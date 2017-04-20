#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_dcap():
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87")
	dcap["phantomjs.page.settings.loadImages"] = False
	return dcap

def main():
	url = "http://36kr.com/newsflashes"
	wd = webdriver.PhantomJS(desired_capabilities=get_dcap() )
	wd.get(url)
	wd.implicitly_wait(3)
	wd.set_page_load_timeout(5)
	wd.set_script_timeout(5)
	# newsList = wd.find_element_by_class_name('sameday_list').text
	newsList = wd.find_element_by_class_name('sameday_list').find_elements_by_tag_name('li')

	li = list()
	for i in newsList:
		li.append(i.find_element_by_class_name('title').text)
		# print(newsList[i].text)
		# s = input()
	# with open('te.md', 'w') as f:
	# 	for i in newsTitle:
	# 		f.write(i.text)
	wd.close()
	return li

# with open('b.html', 'w') as f:
#     f.write(wd.page_source )

# wd.get_screenshot_as_file('01.png')

news = main()
print()
for i in range(10):
	print( news[i] + '\n' )




#	序

	以前都是通过开发者工具追溯数据源，现在试了试`python3` + `selenium` + `phantomjs`，进行资源的自动解析。

	环境搭建略坑。一开始为了图省事，直接在c9上搭建环境，结果死活无法解析，后来在本地重建环境，再试就OK了，连UA都不需要添加。目测可能是ip的问题。
	
#	环境搭建

	*	`phantomjs`使用`npm`进行安装管理

		```bash
		$ sudo apt-get install npm
		$ sudo npm install -g phantomjs-prebuilt
		```

	*	`selenium`使用`pip`进行安装管理

		```bash
		$ sudo pip3 install selenium
		```

#	TODO

	`sqlite/mysql`保存记录`标题`，`时间`，`具体内容`等条目。这个阅读器的初衷是简洁轻量，阅后即焚即可。用数据库纯当练手。

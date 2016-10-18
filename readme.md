#	36kr NewsFlash Reader(Updated on 2016-10-18)

##	CN

前两天偶然发现了 http://new.36kr.com/newsflashes 这个网站，上面会即时更新一些科技时讯，于是就萌生了做个小爬虫来抓取上面新闻的想法(其实应该算是spider，当时还不清除spider 和 crawler 的区别0.0).

**36kr Newsflash Reader** 是专门用来读取上面那个网站的前10条新闻的，如果要用到其他网站，某些地方需要修改.

####	`用法`

这个脚本用Python3.4写的，直接在终端里面敲入以下命令就能运行了:

`$ python3 36kr_newsflash_reader.py`

####	`更多`

刚学python..这个20行的小脚本写了一整天...其实涉及的知识还是很多的，尤其是网络方面。我把基本过程都写在了log.md，另外test文件夹里面是一些测试文件

不过python的表现力足够丰富，尤其是写这样小的自动化脚本，理解起来完全不费力。

> 人生苦短，我用python :)

<br/><br/>

##	EN

**36kr NewsFlash Reader** is a spider to download and show the first 10 news of http://new.36kr.com/newsflashes

PS: While it's specially designed to grab 36kr news, changes are needed if used elsewhere.

####	`Usage`

This Python3.4-based script may be simply used with your Terminal:

`$ python3 36kr_newsflash_reader.py`

####	`More`

More details and reference may be seen in `log.md` and folder `test`

> Life is short, you need Python :)

<br/><br/>

##	Update: `36kr_newsflash_reader_line_by_line.py`

*	修改获取新闻的`url='http://36kr.com/api/newsflash'`，原来的url不知道何时失效。新的api一次只有10条新闻，因此10条后需要重新获取。

*	另外这个版本是另一种阅读方式，即：

1.	运行后打印第一条新闻标题

2.	每次按下`Enter`可以打印一条标题，可以一直按下去获得更多标题

3.	退出：`ctrl+c`或者输入`q`

4.	获取新闻时间：输入`t`



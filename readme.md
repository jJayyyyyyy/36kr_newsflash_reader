# 36kr NewsFlash Reader

### CN

前两天偶然发现了 http://new.36kr.com/newsflashes 这个网站，上面会即时更新一些科技时讯，于是就萌生了做个小爬虫来抓取上面新闻的想法(其实应该算是spider，当时还不清除spider 和 crawler 的区别0.0).

**36kr Newsflash Reader** 是专门用来读取上面那个网站的前10条新闻的，如果要用到其他网站，某些地方需要修改.

#### `用法`

这个脚本用Python3.4写的，直接在终端里面敲入以下命令就能运行了:

`$ python3 36kr_newsflash_reader.py`

#### `更多`

刚学python..这个20行的小脚本写了一整天...其实涉及的内容还是很多的，尤其是网络方面。我把基本过程都写在了log.md，另外test文件夹里面是一些测试文件

不过python的表现力足够丰富，尤其是写这样小的自动化脚本，理解起来完全不费力。

> 人生苦短，我用python :)

<br/><br/>

## EN

**36kr NewsFlash Reader** is a spider to download and show the first 10 news of http://new.36kr.com/newsflashes

PS: While it's specially designed to grab 36kr news, changes are needed if used elsewhere.

#### `Usage`

This Python3.4-based script may be simply used with your Terminal:

`$ python3 36kr_newsflash_reader.py`

#### `More`

More details and reference may be seen in `log.md` and folder `test`

> Life is short, you need Python :)

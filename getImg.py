# -*- coding: UTF-8 -*-
import re
import urllib,urllib2;
 
# 获取网页内容函数 http://service.wifiha.com/face/get
def getHtml(url):
	# 要设置请求头，让服务器知道不是机器人
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	request=urllib2.Request(url,headers=headers);
	page = urllib2.urlopen(request);
	html = page.read()
	return html
	
#通过正则表达式来获取图片地址，并下载到本地
def getImg(html):
	reg = r'src="(.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	for imgurl in imglist:
		print imgurl;
	#通过urlretrieve函数把数据下载到本地的D:\\images，所以你需要创建目录
		urllib.urlretrieve(imgurl, 'D:\\images\\%s.jpg' % x)
		x = x + 1
	
htmlContent=getHtml("http://service.wifiha.com/face/get");
getImg(htmlContent)
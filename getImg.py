# -*- coding: UTF-8 -*-
import re
import urllib,urllib2;
 
# ��ȡ��ҳ���ݺ��� http://service.wifiha.com/face/get
def getHtml(url):
	# Ҫ��������ͷ���÷�����֪�����ǻ�����
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	request=urllib2.Request(url,headers=headers);
	page = urllib2.urlopen(request);
	html = page.read()
	return html
	
#ͨ��������ʽ����ȡͼƬ��ַ�������ص�����
def getImg(html):
	reg = r'src="(.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	for imgurl in imglist:
		print imgurl;
	#ͨ��urlretrieve�������������ص����ص�D:\\images����������Ҫ����Ŀ¼
		urllib.urlretrieve(imgurl, 'D:\\images\\%s.jpg' % x)
		x = x + 1
	
htmlContent=getHtml("http://service.wifiha.com/face/get");
getImg(htmlContent)
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import os

hosturl = 'http://www.360doc.com/content/14/0813/17/15477063_401589947.shtml'
#����header��һ��header����Ҫ����һ������������Ǵ�ץ���İ�������ó��ġ�
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0', 'Referer' : hosturl}
#�򿪵�¼��ҳ�棨����Ŀ���Ǵ�ҳ������cookie����������������post����ʱ����cookie�ˣ������Ͳ��ɹ���
request = urllib2.Request(hosturl,None, headers)
response = urllib2.urlopen(request)
htmldata = response.read()
data=htmldata.decode('utf-8')
pre = '<span id="articlecontent" onmousedown="newhighlight = true;" onmouseup="NewHighlight(event)">'
index1 = data.find(pre) + len(pre)
index2 = data.find('<div id="viewerPlaceHolder" style="width: 717px; height: 700px; display: none;">', index1)
content = data[index1 : index2]
pretitle = '<div class="biaoti2 lf360">'
indextitle1 = data.find(pretitle) + len(pretitle)
indextitle2 = data.find('</div>', indextitle1)
title = data[indextitle1 : indextitle2].replace("\r\n","").strip()
  
print(title)
f = open(title+"_"+hosturl.split("/")[-1],"w")
f.write(content)
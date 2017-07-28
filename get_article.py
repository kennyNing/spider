# -*- coding: UTF-8 -*-
import urllib2
import urllib
import os

hosturl = 'http://www.360doc.com/content/14/0813/17/15477063_401589947.shtml'
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0', 'Referer' : hosturl}
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
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
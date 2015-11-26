# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import sys


url = "http://www.zimuzu.tv/esubtitle"
isTrue = True

target_input = raw_input("请输入你要获取的影视字幕信息：").decode('utf-8')

while(isTrue):
        try:
                request   = urllib2.Request(url)
                response  = urllib2.urlopen(request)
                htmlcode =  response.read().decode('UTF-8', 'ignore')
                pattern = re.compile('<div .*?subtitle-list">.*?<dt.*?<strong.*?<a.*?>(.*?)</a></strong>',re.S)
                items = re.findall(pattern,htmlcode)
                for item in items:
                        pattern = re.compile(target_input,re.S)
                        i = re.findall(pattern,item)
                        if len(i):
                                for it in i:
                                        print i
                                        print "已经更新请下载前往网站…………"
                                        isTrue = False
                                        break
                        else:
                                print "还未更新，请稍后…………"
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason



        

# # -*- coding=UTF-8 -*-
'''
抓取一个网页，每两秒刷新一次，使用正则表达式匹配第一个字幕的变化。如果有变化则发出并且是自己要的则发出警报。
'''

import urllib2
import urllib
import re


target_input = raw_input("请输入您想要获取的字幕名称：").decode('gb2312')

isTrue = True
url = "http://www.zimuzu.tv/esubtitle"
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
                        print "还没有更新，请稍等…………"
                        for it in i:
                                print "已经更新了"
                                isTrue = False


        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason





# -*- coding: gbk -*-
'''
ץȡһ����ҳ��ÿ����ˢ��һ�Σ�ʹ��������ʽƥ���һ����Ļ�ı仯������б仯�򷢳��������Լ�Ҫ���򷢳�������
'''

import urllib2
import urllib
import re
import sys

#һЩ������Ϣ
url = "http://www.zimuzu.tv/esubtitle"
isTrue = True

target_input = raw_input("����������Ҫ��ȡӰ�ӵ���Ļ���ƣ�").decode('gbk')

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
                                        print "�Ѿ�������ǰ����վ���ء�������"
                                        isTrue = False
                                        break
                        else:
                                print "δ���£����Եȡ�������"
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason



        

# -*- coding:utf-8 -*-

import urllib2
import re
import sys
import platform
import logging
import datetime
import time

def targetTitle():
    #配置logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s => %(message)s')
    systemType = platform.system()
    if systemType == 'Windows':
        target = raw_input("请输入要获取字幕的名称关键字：").decode('bgk')
        return target
    elif systemType == 'Linux':
        target = raw_input("请输入要获取字幕的名称关键字：").decode('UTF-8')
        return target
    else:
        logging.info('该程序只支持Linux和中文版Windows全系列版本')
        sys.exit(0)

def getEsubtitleStatus(url):
    target = targetTitle()
    isTrue = False
    encodeTarget = target.encode('utf-8')
    ReleaseTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    while not isTrue:
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            htmlcode = response.read().decode('utf-8', 'ignore')
            regex = '<div .*?subtitle-list">.*?<dt.*?<strong.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?<dd.*?list_a">.*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).*</span>.*</dd>'
            pattern = re.compile(regex,re.S)
            items = re.findall(pattern,htmlcode)
            for item in items:
                if ReleaseTime != item[2]:
                    pattern = re.compile(target, re.S)
                    isUpdate = re.findall(pattern, item[1])
                    if isUpdate:
                        esubUrl = "http://www.zimuzu.tv/"+item[0]
                        logging.info('%s 已经更新，请前往%s下载' %(encodeTarget, esubUrl.encode('utf-8')))
                        isTrue = True
                    else:
                        logging.info('%s还没有更新，信息一下' %encodeTarget)
                        time.sleep(3)
                break
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                logging.warn(e.code)
            if hasattr(e, "reason"):
                logging.warn(e.reason)

if __name__ == '__main__':
    url = "http://www.zimuzu.tv/esubtitle"
    getEsubtitleStatus(url)

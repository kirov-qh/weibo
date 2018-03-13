#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import json
import re
import scrapy
import threading
import time
import random
import requests
from scrapy.http import Request
from weibocontent.items import WeibocontentItem
#from weibocontent.settings import INPUTFILE_POSITION
from scrapy_redis.spiders import RedisCrawlSpider
from redis import Redis

import sys

reload(sys)
sys.setdefaultencoding('utf8')

class SinaSpider(RedisCrawlSpider) :

    name = "weibo"

    allowed_domains = [
     "m.weibo.cn"
    ]

    redis_key = 'weibo:user_url'  # 从redis队列里取得url

    weiboCount = 0

    # # 构建url
    # def start_requests(self):
    #
    #     # 记录当前uid的次序
    #     uidOrder = 1
    #
    #     # 开一个新线程每5秒更新一次ippool
    #
    #     # 从文件里读取ID
    #     f = open(INPUTFILE_POSITION)
    #     for user_id in f.readlines():
    #
    #         user_id = user_id[:-1]
    #
    #         # 构建url获取用户的微博连接
    #         url = 'http://m.weibo.cn/api/container/getIndex?type=uid&value=' + str(user_id)
    #
    #         # 如果能成功连接就进行请求
    #         request = Request(url, meta={'uid': user_id }, callback=self.creat_tables, dont_filter=True)
    #         yield request
    #
    #         # 写入之前将uid写入文件中并记录
    #         out_file = open('./weibocontent/successUid.txt', 'ab+')
    #         out_file.write(user_id)
    #         out_file.write('\n')
    #         out_file.close()
    #         out_file = open('./weibocontent/uidCount.txt', 'ab+')
    #         statement = {"order": uidOrder, "uid": user_id}
    #         out_file.write(json.dumps(statement))
    #         out_file.write('\n')
    #         out_file.close()
    #
    #          # 打印日志
    #         print u'正在读取第 %d 条UID...' % int(uidOrder)
    #         print user_id
    #         uidOrder = uidOrder + 1




    # 通过api传回来的是json格式的数据，我们可以直接将其转成dict格式然后直接抽取
    def parse(self, response):

        uid = response.url[response.url.find('value=') + 6 : ]

        '''
        # 将读取到的UID装入redis中
        retry_time = 0
        while (True) :
            print 'weibo:readed_uid retry...'
            if retry_time >= 10:
                break
            try :
                retry_time = retry_time + 1
                r.lpush('weibo:readed_uid', str(uid).encode('utf-8'))
                break
            except :
                continue
        '''

        print response.url

        # 首先检验uid是否失效
        msg = response.body.find('errmsg')
        retry_time = 0

        if (msg != -1) :
            while (True) :
                print 'weibo:error_uid retry push ...'
                if retry_time >= 10:
                    break
                try :
                    retry_time = retry_time + 1
                    r = redis.Redis(host = '222.27.227.116', port = 6379, db = 0)
                    r.lpush('weibo:error_uid', uid)
                    break
                except :
                    continue
            print u'发现失效uid： ', uid, u' ,失效uid已存入redis中...'
            return

        content = json.loads(response.body)
        containerid = None

        for data in content.get('tabsInfo').get('tabs'):
            if data.get('tab_type') == 'weibo':
                containerid = data.get('containerid')

        # 微博个数
        web_num = content.get('userInfo').get('statuses_count')

        # 获取微博的页数
        page = web_num/10 + 1

        # 轮流每一页都进行爬取
        for i in range(1, page+1):
            if containerid:
                # weibo_url like :  http://m.weibo.cn/api/container/getIndex?type=uid&value=2422828740&containerid=1076032422828740&page=1
                weibo_url = response.url + '&containerid=%s' % containerid + '&page=' + str(i)
                request = Request(weibo_url, meta={'uid': uid, 'containerid':containerid },callback=self.get_weibo, dont_filter=True)
                yield request
            else:
                print '----->> 没有查询到containerid <<-----'

    # 这里将微博的具体内容抽取出来并进行处理，然后将其信息进行封装
    def get_weibo(self, response):
        # 页面的内容
        curPage = response.body
        # \n是正常时回车，\r是win下的回车，这是防止有些微博里有换行而存入时不规整设计的
        curPage = curPage.replace('\n', '').replace('\r\n', '').replace('\r', '')
        content = json.loads(curPage)
        # 迭代到每条微博
        for data in content.get('cards'):
            # card_type分为9和11，11没有内容，9里面是需要的东西
            if data.get('card_type') == 9:

                # 创建一个微博实体
                weiboItem = WeibocontentItem()

                # 抓取微博内容
                weiboDict = data

                # 接下来进行数据的封装
                mblogDict = weiboDict.get('mblog')

                self.weiboCount = self.weiboCount + 1

                # 判断是否为转发的信息
                if mblogDict.get('retweeted_status') is not None :

                    # 该情况下为转发信息
                    weiboItem['isOri'] = False

                    # 封装和原创有关的信息
                    oriWeiboDict = mblogDict.get('retweeted_status')
                    oriUserDict = oriWeiboDict.get('user')

                    # 首先要判断原文是否已删除，已删除则舍弃该条数据
                    if oriUserDict is not None :
                        weiboItem['oriId'] = oriUserDict.get('id')
                        weiboItem['oriName'] = oriUserDict.get('screen_name')

                        weiboItem['oriWeiboId'] = oriWeiboDict.get('idstr')
                        weiboItem['oriText'] = oriWeiboDict.get('text')
                        weiboItem['oriPicInfo'] = oriWeiboDict.get('pics')
                        weiboItem['oriRepost'] = oriWeiboDict.get('reposts_count')
                        weiboItem['oriAttu'] = oriWeiboDict.get('attitudes_count')
                        weiboItem['oriComment'] = oriWeiboDict.get('comments_count')
                        weiboItem['oriFrom'] = oriWeiboDict.get('source')
                        weiboItem['oriTime'] = self.time_form(oriWeiboDict.get('created_at').encode('utf-8'))
                    else :
                        continue

                    # 封装和转发有关的信息
                    reUserDict = mblogDict.get('user')

                    weiboItem['reId'] = reUserDict.get('id')
                    weiboItem['reName'] = reUserDict.get('screen_name')

                    weiboItem['weiboId'] = mblogDict.get('idstr')
                    weiboItem['reWeiboId'] = mblogDict.get('idstr')
                    weiboItem['reText'] = mblogDict.get('text')
                    weiboItem['rePicInfo'] = mblogDict.get('pics')
                    weiboItem['reRepost'] = mblogDict.get('reposts_count')
                    weiboItem['reAttu'] = mblogDict.get('attitudes_count')
                    weiboItem['reComment'] = mblogDict.get('comments_count')
                    weiboItem['reFrom'] = mblogDict.get('source')
                    weiboItem['reTime'] = self.time_form(mblogDict.get('created_at').encode('utf-8'))

                    # 封装其它数据
                    weiboItem['weiboId'] = mblogDict.get('idstr')
                    weiboItem['weiboUrl'] = weiboDict.get('scheme')
                    weiboItem['crawlTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

                else :
                    # 该情况下为原创信息
                    weiboItem['isOri'] = True

                    # 封装和原创有关的信息
                    oriUserDict = mblogDict.get('user')

                    weiboItem['weiboId'] = mblogDict.get('idstr')

                    weiboItem['oriId'] = oriUserDict.get('id')
                    weiboItem['oriName'] = oriUserDict.get('screen_name')

                    weiboItem['oriWeiboId'] = mblogDict.get('idstr')
                    weiboItem['oriText'] = mblogDict.get('text')
                    weiboItem['oriPicInfo'] = mblogDict.get('pics')
                    weiboItem['oriRepost'] = mblogDict.get('reposts_count')
                    weiboItem['oriAttu'] = mblogDict.get('attitudes_count')
                    weiboItem['oriComment'] = mblogDict.get('comments_count')
                    weiboItem['oriFrom'] = mblogDict.get('source')
                    weiboItem['oriTime'] = self.time_form(mblogDict.get('created_at').encode('utf-8'))

                    # 封装其它数据
                    # 这里不能用weiboItem['xxx'] = weiboItem['yyy']的方式来进行赋值

                weiboItem['weiboUrl'] = weiboDict.get('scheme')
                weiboItem['crawlTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

                # 将读到的weiboId存入redis中，这样可以有效得到已经爬取的weibo的数量
                #r.lpush('weibo:readed_weiboId', str(mblogDict.get('user').get('id')))

                # 打印提示信息
                print u'正在处理第 %d 条微博：  %s  %s' % (self.weiboCount, weiboItem['weiboId'], str(time.strftime('%H:%M:%S', time.localtime(time.time()))))
                yield weiboItem
                # print weiboItem['oriName']


    # 回溯发表微博时间
    def time_form(self, time_str):
        if '刚刚' in time_str:
            real_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
            return real_time
        elif '分钟' in time_str:
            time_str = time_str.split('分钟')
            seconds = int(time_str[0]) * 60
            real_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - seconds))
            return real_time
        elif '小时' in time_str:
            time_str = time_str.split('小时')
            seconds = int(time_str[0]) * 60 * 60
            real_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - seconds))
            return real_time
        elif '今天' in time_str:
            time_str = time_str.split('今天')
            today = time_str[1]
            real_time = time.strftime('%Y-%m-%d', time.localtime(time.time())) + today
            return real_time
        elif '昨天' in time_str:
            time_str = time_str.split('昨天')
            yesterday = time_str[1]
            real_time = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60)) + yesterday
            return real_time
        elif len(time_str) == 5:
            real_time = time.strftime('%Y-', time.localtime(time.time())) + time_str
            return real_time
        else:
            real_time = time_str
            return real_time













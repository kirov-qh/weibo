#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
爬取的是wap站上的用户信息
'''
import json
import random
import re
from types import NoneType

import scrapy
import requests
import time
from scrapy import Request
from scrapy.selector import Selector
from sina.items import testItem, userInfoItem
from sina.cookies import cookieList
from sina.settings import REQUEST_INTREVAL
from sina.settings import INPUTFILE_LOCATION


class InfoSpider(scrapy.Spider) :

    # 该爬虫的名字
    name = "infoSpider"

    # 允许通过的域
    allowed_domains = [
        "weibo.cn"
    ]

    # ip池
    # ip池暂时不用了，因为发现免费的代理都不好用，代码都注释掉了，并没有删掉
    #IPPOOL = []

    # cookie池
    # cookies.cookieList中是直接从浏览器中复制的cookie，这里需要把他们转变成dict的list集合
    COOKIEPOOL = [

    ]

    # 使用的cookie、user-agent由中间件处理

    # 从文件中读取uid来构建url
    # 这里面涉及到cookie池的构建，ip代理池的构建，参数控制以及信息打印
    def start_requests(self):

        # 初始化ip池(弃用)
        '''
        print u'正在初始化IPPOOL...'
        ipUrl = 'http://www.xicidaili.com/nn/'
        request = Request(ipUrl, callback=self.parseIP, dont_filter = True)
        yield request
        '''


        # 从setting中读取，设置请求频率
        request_interval = REQUEST_INTREVAL

        # 从setting中读取，设置文件的读取位置
        inputfile_location = INPUTFILE_LOCATION

        # 用于计数爬取了多少条用户记录
        d = 0

        # 用于控制IPPOOL的更新
        #ipflushCount = 0

        print u'初始化cookie池...'
        print u'cookie池的期望大小为：  ' , cookieList.__len__()

        # 初始化cookie池
        cookiepool = []

        # cookies.cookieList中是为处理的cookie，这里需要处理一下然后存到本地的COOKIEPOOL中
        for string in cookieList :
            # cookies.cookieList中的cookie是字符串，我们需要把它转化成字典形式
            single_cookie = {}
            # 所以这里我们可以利用一下Python的字符串方法分词
            for str_spl in  str(string).split(';') :
                # 整个字符串分解之后再利用分词将每个小字符串化成key:value的形式，也就是json的格式
                cookie_spl = str_spl.split("=")
                # strip()方法用于去除字符串两边的空格
                key = cookie_spl[0].strip()
                value = cookie_spl[1].strip()
                # ALF和SSOLoginState两个属性必须是int类型，不然会报错
                if (key == 'ALF') | (key == 'SSOLoginState'):
                    value = int(value)
                single_cookie[key] = value
            cookiepool.append(single_cookie)
            print u'新cookie加入cookie池...'



        # 处理完cookie之后把缓存的结构化的cookie直接复制到COOKIEPOOL
        self.COOKIEPOOL = cookiepool
        print u'cookie池初始化完成，大小为：  ', self.COOKIEPOOL.__len__()
        time.sleep(1.5)



        # 打印一些有的没的的日志
        print '\n------------------------------------\n'
        print u'当前请求的频率为：  每条请求间隔时间 ' , request_interval, u'秒\n'
        print u'当前输入文件的位置为：  ', inputfile_location, '\n'
        print '------------------------------------\n'
        print u'开始爬虫进程...'
        time.sleep(1.5)


        # 读取文件中的uid
        f = open(inputfile_location)
        for id in f.readlines() :

            # d计数器只是计算已经读了多少条用户id而已，从1开始计数
            d = d + 1

            # 每秒上限速度4条
            time.sleep(request_interval)

            # 控制IPPOOL的计数器每秒会加一，每次在发出IPPOOL的请求时候会清零
            # ipflushCount = ipflushCount + 1


            # 首先爬代理ip，把爬下来的ip放在IPPOOL中，每爬20条数据更新一次ip池(已弃用)
            '''
            if (ipflushCount == 20):
                # 首先检查IPPOOL中随机取得的代理是否有效
                #while self.IPPOOL.__len__() != 0 :
                proxy = random.choice(self.IPPOOL)

                    try :
                        protocol = (str(proxy).split(":"))[0]
                        proxies = {protocol: proxy}
                        # 如果该代理ip能正常访问则跳出循环
                        if requests.get('http://www.xicidaili.com/nn/', proxies=proxies, timeout=2).status_code == 200:
                            request.meta['proxy'] = proxy
                            break
                        else :
                            self.IPPOOL.remove(proxy)
                            print u'代理 ', proxy, u'已失效并已去除，当前IPPOOL大小为：  ' , self.IPPOOL.__len__()
                    except:
                        # 如果代理失效则去除该代理IP并重新随机选择高匿代理IP
                        self.IPPOOL.remove(proxy)
                        print u'代理 ', proxy, u'已失效并已去除，当前IPPOOL大小为：  ' , self.IPPOOL.__len__()
                        continue
            '''

            # 开启爬取西刺代理的IP的进程
            '''
                request = Request(ipUrl, callback=self.parseIP, dont_filter=True)
                request.meta['proxy'] = proxy
                ipflushCount = 0
                yield request
            '''
            #<end : if>




            # 该路径为用户的wap端首页，可以取到用户的微博数、关注数、粉丝数
            urlNum = "https://weibo.cn/u/%d" % int(id)

            # 该路径为用户的wap端个人信息页面，可以获取用户的其他信息
            urlInfo = 'https://weibo.cn/%d/info' % int(id)

            # 如果IPPOOL不为空，则从IPPOOL中去高匿代理IP
            # 首先检查IPPOOL中随机取得的代理是否有效
            '''
            while self.IPPOOL.__len__() > 0 :
                proxy = random.choice(self.IPPOOL)
                try :
                    protocol = 'https' if 'https' in proxy else 'http'
                    proxies = {protocol: proxy}
                    if requests.get('http://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200 :
                        request.meta['proxy'] = proxy
                        print request.meta['proxy']
                        break
                    else :
                        self.IPPOOL.remove(proxy)
                        print u'代理 ', proxy, u'已失效并已去除，当前IPPOOL大小为：  ' , self.IPPOOL.__len__()
                except:
                    # 如果代理失效则去除该代理IP并重新随机选择高匿代理IP
                    self.IPPOOL.remove(proxy)
                    print u'代理 ', proxy, u'已失效并已去除，当前IPPOOL大小为：  ' , self.IPPOOL.__len__()
                    continue
          '''

            # 设置请求的路径和携带的信息
            request = Request(urlNum, meta={'uid': id , 'urlInfo': urlInfo }, callback=self.parseNum)

            # 设置随机cookie
            request.cookies = random.choice(self.COOKIEPOOL)
            #print request.cookies

            # 设置IP代理
            '''
            if self.IPPOOL.__len__() > 0 :
                request.meta['proxy'] = random.choice(self.IPPOOL)
           '''

            # 输出日志并开始爬
            print u'读取第', d, u'条用户uid：  '  , id

            yield request

        #<end : for id in f.readlines()>
    #<end : start_requests>

    # 这里设置爬取时间、用户uid、爬用户的关注、粉丝、微博数
    def parseNum(self, response):

        # 声明item
        infoItem = userInfoItem()

        # 封装爬取的uid和时间
        infoItem['uid'] = response.meta['uid']
        time.localtime(time.time())
        infoItem['crawlTime']  = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # 爬取粉丝数、关注数、微博数
        sel = Selector(response)
        infoItem['weiboNum'] = int(sel.xpath('//div[@class="tip2"]/span/text()').extract_first()[3: -1])
        infoItem['fansNum'] = int(sel.xpath('//div[@class="tip2"]/a[1]/text()').extract_first()[3: -1])
        infoItem['conNum'] = int(sel.xpath('//div[@class="tip2"]/a[2]/text()').extract_first()[3: -1])

        # 爬取详细页面的连接并跳转
        url = response.meta['urlInfo']
        request = Request(url, meta={'infoItem': infoItem}, callback=self.parseInfo)
        request.cookies = random.choice(self.COOKIEPOOL)

        '''
        # 这里同样设置代理，但是没有检验机制
        if self.IPPOOL.__len__() != 0 :
            proxy = random.choice(self.IPPOOL)
            request.meta['proxy'] = proxy
        '''

        yield request
    #<end : parseNum>

    # 这里跳转到了用户详细信息页面，爬取用户的详细信息
    def parseInfo(self, response):

        # 取出已经存好粉丝、关注、微博、uid、时间的item
        infoItem = response.meta['infoItem']

        # 继续往里面存其他用户数据
        sel = Selector(response)

        # 获取头像url
        infoItem['headUrl'] = sel.xpath('//div[@class="c"][1]/img[1]/@src').extract_first()

        # 判断是头像url是否为空，为空则pass掉该条数据
        if type(infoItem['headUrl']) == NoneType :
            return

        # 获取昵称和其它信息
        text1 = ";".join(sel.xpath('body/div[@class="c"]/text()').extract())         # 获取标签里的所有text()
        infoItem['nickName'] = re.findall(u'\u6635\u79f0[:|\uff1a](.*?);', text1)      # 昵称
        infoItem['gender'] = re.findall(u'\u6027\u522b[:|\uff1a](.*?);', text1)        # 性别
        infoItem['place'] = re.findall(u'\u5730\u533a[:|\uff1a](.*?);', text1)         # 地区（包括省份和城市）
        infoItem['signature'] = re.findall(u'\u7b80\u4ecb[:|\uff1a](.*?);', text1)    # 个性签名
        infoItem['birthday']  = re.findall(u'\u751f\u65e5[:|\uff1a](.*?);', text1)    # 生日
        infoItem['sexori'] = re.findall(u'\u6027\u53d6\u5411[:|\uff1a](.*?);', text1) # 性取向
        infoItem['marriage'] = re.findall(u'\u611f\u60c5\u72b6\u51b5[:|\uff1a](.*?);', text1)  # 婚姻状况

        yield infoItem

    #<end : parseInfo>

    # 这里通过爬取http://www.data5u.com/上的ip和端口号更新IP池
    # 该方法暂时不会用到，因为好用的IP代理必须花钱买，挺贵的，后续测试发现不需要ip代理，控制cookie池就可以规避风险
    def parseIP(self, response) :
        print u'更新IP池...'
        # 创建空列表用来存最新的ip
        ipList = []

        sel = Selector(response)
        # 通过循环向IP池中填充最多15个有效IP
        for num in range(2, 12) :

            # 获取ip地址
            xpath = '//table[@id="ip_list"]/tr[' + str(num) + ']/td[2]/text()'
            curip = sel.xpath(xpath).extract_first()
            # 获取端口
            xpath = '//table[@id="ip_list"]/tr[' + str(num) + ']/td[3]/text()'
            curport = sel.xpath(xpath).extract_first()
            # 获取类型
            xpath = '//table[@id="ip_list"]/tr[' + str(num) + ']/td[6]/text()'
            curproxy = sel.xpath(xpath).extract_first()
            # 利用拼凑出代理地址
            proxy = str(curproxy).lower() + "://" + str(curip) + ":" + str(curport)

            # 检测高匿代理的速度
            xpath = '//table[@id="ip_list"]/tr[' + str(num) + ']/td[7]/div/@title'
            speed = float(sel.xpath(xpath).extract_first()[:-1])
            # 检测高匿代理的连接时间
            xpath = '//table[@id="ip_list"]/tr[' + str(num) + ']/td[8]/div/@title'
            connecttime = float(sel.xpath(xpath).extract_first()[:-1])

            # 如果高匿代理的速度和连接时间大于0.5，则舍弃该代理
            if (speed > 1.0) | (connecttime > 1.0) :
                continue

            # 检测代理是能链接到wap端的微博页面
            try :
                protocol = 'https' if 'https' in proxy else 'http'
                proxies = {protocol: proxy}
                requests.get('http://www.baidu.com/', proxies=proxies, timeout=2).status_code == 200
                print u'新代理IP ', proxy , u'加入，速度为 ', str(speed), u'秒， 连接时间为 ', str(connecttime), u'秒'
            except:
                continue

            # 如果闯过了上述关卡则证明代理是一个优秀的免费代理，把它加入IPPOOL中
            ipList.append(proxy)

        # 将缓存线程池的列表复制给线程池
        self.IPPOOL = ipList
        print u'线程池更新完毕， 更新后大小为：  ', self.IPPOOL.__len__(),  self.IPPOOL
    #<end : parseIP >

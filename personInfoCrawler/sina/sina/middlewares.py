#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from sina.cookies import cookieList
from sina.user_agents import agents, mobileAgents


# 随机更换user-agent
class UserAgentMiddleware(object):

    def process_request(self, request, spider):
        agent = random.choice(mobileAgents)
        request.headers["User-Agent"] = agent
        request.headers["Connection"] = 'keep-alive'
        request.headers["Accept-Language"] = 'zh-CN,zh;q=0.8'
        request.headers["Accept-Encoding"] = 'gzip, deflate, sdch'
        request.headers["Accept"] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'


# 设置cookies
class CookiesMiddleware(object):
    # 随机选取列表中的cookies
    def process_request(self, request, spider):
        cookie = random.choice(cookieList)
        request.cookies = cookie


# 设置代理ip
# class ProxyMiddleware(object) :
#    # 随机选取列表中的代理ip地址
#    def process_request(self, request, spider) :
#        request.meta['proxy'] = "http://" + random.choice(ip)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
该脚本用于创建redis
'''
from redis import Redis

# 构建url获取用户的微博连接并添加到redis队列里

r = Redis()

# 输入文件
f = open('./input.txt')

order = 1

for user_id in f:
    user_id = user_id[:-1]
    url = 'http://m.weibo.cn/api/container/getIndex?type=uid&value=' + str(user_id)
    print u'正在将第 %8d 个URL加入redis队列中：  %s ' % (order, url)
    order = order + 1
    r.lpush('weibo:user_url', url)
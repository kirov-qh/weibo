#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2422828740
2603926877
1583089553
1806928880
2691144174
2803080370
'''

import scrapy
from scrapy import Item,Field


class WeibocontentItem(scrapy.Item):
    # define the fields for your item here like:

    # 当前博主相关信息
    weiboId = Field()    # 当前微博的ID，如果是原创则不必说，如果是转发则是转发后的微博的ID，数据库中将其作为主键
    weiboUrl = Field()   # 当前微博的URL，如果是原创则不必说，如果是转发则是转发后的微博的URL

    # 微博属性
    isOri = Field()        # 是否原创：是（True），不是（False）

    # 微博的原创信息（无论是否转发都存原创的信息）
    oriWeiboId = Field()   # 原创微博的ID

    oriId = Field()        # 原创人的ID
    oriName = Field()      # 原创人的昵称

    oriText = Field()      # 原创的文字内容
    oriPicInfo = Field()   # 原创的图片信息，这里没有进行再次细化，因为那样在保存起来很麻烦，虽然没有细化但是粗细度也可以接受，处理起来不会太困难
    oriRepost = Field()    # 原创博文的转发次数
    oriAttu = Field()      # 原创博文的点赞数
    oriComment = Field()   # 原创博文的评论数
    oriFrom = Field()      # 原创博文的来源（设备）
    oriTime = Field()      # 原创博文的发布时间

    # 微博的转发信息
    reWeiboId = Field()    # 转发后的微博的ID

    reId = Field()         # 转发人的ID
    reName = Field()       # 转发人的昵称

    reText = Field()       # 转发时的文字内容
    rePicInfo = Field()    # 转发时的图片内容
    reRepost = Field()     # 转发博文从此处再次被转发的次数
    reAttu = Field()       # 转发博文在此处的点赞数
    reComment = Field()    # 转发博文在此处的评论数
    reFrom = Field()       # 转发博文的来源（设备）
    reTime = Field()       # 转发博文的发布时间

    # 爬虫属性
    crawlTime = Field()    # 爬虫爬取的时间 √



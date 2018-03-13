#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class testItem(Item) :
    body = Field()


class userInfoItem(Item) :

    uid = Field()       # 用户uid
    crawlTime = Field() # 抓取的时间

    conNum = Field()    # 关注数
    fansNum = Field()   # 粉丝数
    weiboNum = Field()  # 微博数

    headUrl = Field()   # 用户头像图片的url

    nickName = Field()  # 昵称
    gender = Field()    # 性别
    place = Field()     # 地区
    birthday = Field()  # 生日
    sexori = Field()    # 性取向
    marriage = Field()  # 婚姻状况
    signature = Field() # 个性签名





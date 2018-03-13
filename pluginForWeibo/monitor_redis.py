#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
用于实时检测redis的状态，在频幕上打印
'''

import redis
import pymongo
import time



# 检测的时间间隔
TIME_INTERVAL = 1
# 初始URL的个数
INIT_URL_NUM = 957651
# 操作系统类型
OP_TYPE = 'WINDOWS' # 'LINUX'
# 单条数据磁盘占用（kb）
SINGLE_DATA_ROM = 2.01
# 爬虫节点数量
SPIDER_NUMBER = 12
# 微博总数
WIEBO_SUMNUM = 827363054


def calculate_time() :
    # 计算IP的更新时间间隔
    time_last = str(r.lindex('weibo:refreshTime', 0))[-8: ].strip().split(':')
    time_earlier =  str(r.lindex('weibo:refreshTime', 1))[-8: ].strip().split(':')
    hour = int(time_last[0]) - int(time_earlier[0])
    minute = int(time_last[1]) - int(time_earlier[1])
    second = int(time_last[2]) - int(time_earlier[2])
    second_interval = hour*60*60 + minute*60 + second*1
    return second_interval

# 链接redis
r = redis.Redis(host = '222.27.227.xxx', port = 6379, db = 0)

# 连接数据库
connection_a = pymongo.MongoClient('222.27.227.xxx', 27017)
connection_b = pymongo.MongoClient('222.27.227.xxx', 27017)
connection_c = pymongo.MongoClient('222.27.227.xxx', 27017)
connection_d = pymongo.MongoClient('222.27.227.xxx', 27017)

database_a = connection_a.Sina
database_b = connection_b.Sina
database_c = connection_c.Sina
database_d = connection_d.Sina

collection_a = database_a.weibo
collection_b = database_b.weibo
collection_c = database_c.weibo
collection_d = database_d.weibo

# 赋初值
count_dba = collection_a.count()
count_dbb = collection_b.count()
count_dbc = collection_c.count()
count_dbd = collection_d.count()
count_dba_old = 0
count_dbb_old = 0
count_dbc_old = 0
count_dbd_old = 0
if (OP_TYPE == 'WINDOWS'):
    print_line = u'————————————————————————————————————————————'
else :
    print_line = u'————————————————————————————————————————————————————————————————————————————————————————'

print u'\n\n-->>     redis监测开始执行     <<-- \n\n'

# 循环的次数，也就是时间数
rotate_time = 1
# 单秒总的数据增量
second_increase = 1
# 近期一分钟的数据增量
minute_increase = 1
# 总的增量
sum_increase = 1
# 开始的时间
init_time = time.time()
# 上一次记录的时间
last_time = 0
# 当前时间
cur_time = 0

# 防止除零
time.sleep(1)

while (True):


    count_dba = collection_a.count()
    count_dbb = collection_b.count()
    count_dbc = collection_c.count()
    count_dbd = collection_d.count()

    if count_dba_old != 0:
        # 计算上一秒的增量
        second_increase = count_dba - count_dba_old + count_dbb - count_dbb_old + count_dbc - count_dbc_old + count_dbd - count_dbd_old

        # 计算总增量
        sum_increase = sum_increase + second_increase

    #
    cur_time = time.time()


    # 打印在屏幕上
    print print_line
    print u'  COUNT: %-8d         TIME: %-25s' % (rotate_time, str(time.strftime(' %Y-%m-%d   %H:%M:%S ', time.localtime(time.time()))))
    print print_line
    print u'| 请求池容量： %-10d' % r.llen("weibo:requests"),
    print u' URL池容量：   %-10d' % r.llen("weibo:user_url"),
    print u' 已读取URL数：  %-20d|' % (INIT_URL_NUM - r.llen("weibo:user_url"))
    print u'| IP池容量：   %-10d' % r.llen("weibo:ippool"),
    print u' IP池更新间隔： %-10d' % calculate_time(),
    print u'IP池更新时间：%-20s |' % r.lindex('weibo:refreshTime', 0)

    print print_line
    ippool_ori = r.lrange('weibo:ippool', 0, r.llen('weibo:ippool'))
    for index in range(0, ippool_ori.__len__()) :
        if index % 3 == 0:
            print '| %-26s' % ippool_ori[index],
        elif index % 3 == 1:
            print '  %-25s  ' % ippool_ori[index],
        elif index % 3 == 2:
            print '  %-25s  |' % ippool_ori[index]
    if ippool_ori.__len__() % 3 == 1 :
        print '  %-25s    %-25s  |' % ('','')
    elif ippool_ori.__len__() % 3 == 2 :
        print '  %-25s  |' % ''
    print print_line
    print u'| 数据库：      %-18s%-18s%-18s%-18s|' %('hadoop-104','hadoop-107','hadoop-110','hadoop-113')
    print u'| 数据数目：    %-18d%-18d%-18d%-18d|' %(count_dba,count_dbb,count_dbc,count_dbd)
    print u'| 单秒数据增量：%-18d%-18d%-18d%-18d|' %(count_dba - count_dba_old,count_dbb - count_dbb_old,count_dbc - count_dbc_old,count_dbd - count_dbd_old)
    print u'| 磁盘占用：    %-18s%-18s%-18s%-18s|' %(str(count_dba * SINGLE_DATA_ROM/1024)[:-6] + ' MB',
                                                str(count_dbb * SINGLE_DATA_ROM/1024)[:-6] + ' MB',str(count_dbc * SINGLE_DATA_ROM/1024)[:-6] + ' MB',str(count_dbd * SINGLE_DATA_ROM/1024)[:-6] + ' MB')
    print print_line
    print u'| 当前爬取速率： %-8s' % (str((count_dba - count_dba_old + count_dbb - count_dbb_old + count_dbc - count_dbc_old + count_dbd - count_dbd_old) * 1.0/(cur_time - last_time))[0:6] + '/s'),
    print u'  当前单机速率： %-14s' % (str(((count_dba - count_dba_old + count_dbb - count_dbb_old + count_dbc - count_dbc_old + count_dbd - count_dbd_old) * 1.0)/(cur_time - last_time)/12.0)[0:8] + '/s'),
    print u' 总爬取速率： %-16s|' % (str((sum_increase * 1.0)/(cur_time - init_time))[0:14] + '/s')
    print u'| 集群大小：     %-8d' % SPIDER_NUMBER,
    print u'  数据总数：     %-14d' % (count_dba+count_dbb+count_dbc+count_dbc),
    print u' 磁盘总占用： %-16s|' % (str(count_dba * SINGLE_DATA_ROM/(1024*1024) + count_dbb * SINGLE_DATA_ROM/(1024*1024) + count_dbc * SINGLE_DATA_ROM/(1024*1024) + count_dbd * SINGLE_DATA_ROM/(1024*1024))[0:12] + ' GB ')
    print print_line
    print u'| 剩余URL：  %-12s' % (str(((r.llen("weibo:user_url") * 1.0) / (INIT_URL_NUM * 1.0)) * 100)[0:10] + ' %'),
    print u'  剩余数据：     %-14s' % (str( 100.0 - (((count_dba+count_dbb+count_dbc+count_dbd) * 1.0)/ (WIEBO_SUMNUM * 1.0 )) * 100)[0:10] + ' %'),
    print u' 预计剩余时间：%-14s|' % (str(((WIEBO_SUMNUM * 1.0)/((sum_increase * 1.0)/(cur_time - init_time)))/(60.0 * 60.0 * 24.0))[0:10] + ' DAY ')
    print print_line
    print '\n'


    #
    count_dba_old = count_dba
    count_dbb_old = count_dbb
    count_dbc_old = count_dbc
    count_dbd_old = count_dbd

    # 休眠
    rotate_time = rotate_time + 1
    last_time = cur_time
    time.sleep(TIME_INTERVAL)

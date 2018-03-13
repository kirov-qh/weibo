# -*- encoding:utf-8 -*-

'''
从文件中读取数据并转换为dict类型
存储进mongodb中
'''

import pymongo
import json
import time


# connect database
connection = pymongo.MongoClient('222.27.227.110', 27017)
database = connection.Sina
collection = database.info

print collection

inp_file = open('./result_files/weibo_personInfo.json', 'rb')
error_file = open('./result_files/error_details.json', 'wb')

lineList = inp_file.readlines()

index = 1
errorCount = 0

for index in  range(0, lineList.__len__()) :

    line = lineList[index]
    line = line.replace('\\', '\\\\')

    try :
        lineDict = json.loads(line)
    except :
        # 这种解码用于避免\ufeff错误
        line = line.decode('utf-8-sig')
        try :
            lineDict = json.loads(line)
        except :
            errorCount = errorCount + 1
            error_file.write('------------------------------')
            error_file.write('order number is :  ')
            error_file.write(str(index))
            error_file.write('usr uid is :  ')
            error_file.write(line[line.find('weiboNum') + 10: line.find('uid') - 3])
            continue

    lineID = collection.insert_one(lineDict).inserted_id

    print u'正在存储第 %8d 条数据  共 %8d 条数据  ID为 %s 丢失信息个数为 %4d' % (index, lineList.__len__(), lineDict['uid'], errorCount)
    index = index + 1

error_file.write('------------------------------')
error_file.close()






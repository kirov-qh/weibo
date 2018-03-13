#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
back mongodb data into data node server
'''

import pymongo
# import threading
from bson import json_util as jsonb
import time

# class BackUpMongodb(threading.Thread) :
class BackUpMongodb() :

    oriMongodbClient = None
    tarMongodbClient = None

    oriMongodbIP = ""
    tarMongodbIP = ""

    oriMongodb = None
    tarMongodb = None

    oriMongodbDataCount = 0
    tarMongodbDataCount = 0

    saveErrorCount = 0

    initailTime = 0



    # initail
    def __init__(self, oriMongodbIP, tarMongodbIP):

        #super(BackUpMongodb, self).__init__()

        # connect mongodbs
        try :

            self.oriMongodbIP = oriMongodbIP
            self.tarMongodbIP = tarMongodbIP

            print '[DEBUG] : original mongodb ip is : ', oriMongodbIP
            print '[DEBUG] : target mongodb ip is : ', tarMongodbIP

            # create client
            self.oriMongodbClient = pymongo.MongoClient(oriMongodbIP, 27017)
            self.tarMongodbClient = pymongo.MongoClient(tarMongodbIP, 27017)

            #
            print '[DEBUG] : get clients successfully'

            # connect collection
            self.oriMongodb = self.oriMongodbClient.Sina
            self.oriMongodb = self.oriMongodb.weibo
            self.tarMongodb = self.tarMongodbClient.Sina
            self.tarMongodb = self.tarMongodb.weibo

            print '[DEBUG] : connection has been built successfully'

            self.oriMongodbDataCount = self.oriMongodb.count()
            self.tarMongodbDataCount = self.tarMongodb.count()

            print '[DEBUG] : original mongodb current data number is : ', self.oriMongodbDataCount
            print '[DEBUG] : target mongodb current data number is : ', self.tarMongodbDataCount

            # self.dataCollection = self.oriMongodb.find()

            time.sleep(1)

            self.initailTime = time.time()

        except :
            print '\n[ERROR]: connecting to mongodb failed '
            exit()

    # def run(self, rangeIndex, threadNumber):
    def mainFunction(self):

        # calculate range for threads
        #startCount = (self.oriMongodbDataCount / int(threadNumber)) * int(rangeIndex)
        #endCount = (self.oriMongodbDataCount / int(threadNumber)) * (int(rangeIndex) + 1)

        startCount = 0
        endCount = self.oriMongodbDataCount

        # if (threadNumber - 1) == rangeIndex :
        #     endCount = self.oriMongodbDataCount

        # print infomation
        # print 'New thread initailed'
        # print 'current thread get data from ', startCount, ' to ', endCount

        # get from mongodb but do not delete from original mongodb
        # batch insert every time 100 count

        startPosition = int(startCount / 10000)
        endPosition = int(endCount / 10000) + 1

        # transformer cursor to list, which is failed because of the memory overflow
        # dataCollectionList = jsonb.dumps(list(self.dataCollection))

        for index in range(startPosition, endPosition) :

            # try :
            # dataList = []

            # if (index == endPosition - 1) :
            #     for datacount in range(index * 1000, endCount) :
            #         dataList.append(self.dataCollection[datacount])
            # else :
            #     for datacount in range(index * 1000, (index + 1) * 1000):
            #         dataList.append(self.dataCollection[datacount])

            try :
                dataList = list(self.oriMongodb.find().skip(index * 10000).limit(10000))

                if dataList.__len__() > 0 :
                    self.tarMongodb.insert(dataList)
                else :
                    print '[DEBUG] : empty input list'
            except :
                self.saveErrorCount += 1
                print '[ERROR] : error occured during transfer saving data, current error occured number is ', self.saveErrorCount

            # if (index == endPosition - 1) :
            #     self.tarMongodb.bulk_write(self.dataCollection[index * 100 : endCount])
            # else :
            #     self.tarMongodb.bulk_write(self.dataCollection[index * 100 : (index + 1) * 100])
            # except :
            #     self.saveErrorNumber += 1
            #     print 'One more saving error occured  current saving error number is :', self.saveErrorNumber

            print '[INFO]   : data save successfully,  index is [ ', index * 10000 , ', ', ((index + 1) * 10000 - 1) , '] , ',\
                (float(self.oriMongodbDataCount - ((index + 1) * 10000 - 1)) * 100.0 / float(self.oriMongodbDataCount)),'% left, current used time is : ', time.time() - self.initailTime

            # 1,000,000 insert restart connection for one time
            if index % 100 == 0 and index != 0 :
                try :
                    print '[DEBUG] : rebuilding mogno connection -----'
                    self.oriMongodb = None
                    self.oriMongodbClient.close()
                    print '[DEBUG] : close original connection successfully '
                    self.oriMongodbClient = pymongo.MongoClient(self.oriMongodbIP, 27017)
                    self.oriMongodb = self.oriMongodbClient.Sina
                    self.oriMongodb = self.oriMongodb.weibo
                    print '[DEBUG] : start new connection successfully '
                except :
                    print '[ERROR] : error occured during restart connection '
                    time.sleep(5)


        print '[DEBUG] : transfer saving finished'
        print '[DEBUG] : used time : ', time.time() - self.initailTime
        print '[DEBUG] : error number : ', self.saveErrorCount
        print '[DEBUG] : original mongodb IP : ', self.oriMongodbIP
        print '[DEBUG] : target mongodb IP : ', self.tarMongodbIP
        print '[DEBUG] : correct data number is : ', self.oriMongodbDataCount
        print '[DEBUG] : true data number is : ', self.tarMongodb.count()




# main function
if __name__ == "__main__" :

    # THREAD_NUMBER = 5
    ORI_MONGODB_IP = "222.27.227.104"   # 104, 107, 110, 113
    TAR_MONGODB_IP = "222.27.227.131"   # 131, 132

    # print 'thread number is ', THREAD_NUMBER

    # for index in range(0, THREAD_NUMBER) :

    BackUpMongodb(ORI_MONGODB_IP, TAR_MONGODB_IP).mainFunction()

    # .run(index, THREAD_NUMBER)





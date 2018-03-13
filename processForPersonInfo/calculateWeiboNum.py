# -*- encoding:utf-8 -*-

import json
import time

'''
将文件中的数据转存到mongodb中
'''

# 将分开的各个文件中的信息整合到一个文件中，并且将uid中的\n去除，将分割在多行的json弄在同一行上
weibo_file = open(u'./result_files/个人信息(按条分隔).json', 'wb+')

#
weibo_file_oneline = open(u'./result_files/个人信息(无分隔).json', 'wb+')

if __name__ == "__main__" :

    allWeiboNum = 0
    userNum = 0

    for order in range(1, 11) :

        file_path = u'./files/文件%d.json' % order

        # 打开文件分别读取每条数据
        f = open(file_path, 'r')

        lineList = f.readlines()
        print u'计算的文件为：  ', file_path
        print u'文件总行数为：  ', lineList.__len__()
        time.sleep(2)

        index = 1
        weiboNum = 0

        # 从字符串的角度来找微博数
        for line in lineList :
            if line.find('weiboNum') != -1 :
                weiboNum = weiboNum + int(line[line.find('weiboNum') + 10: line.find('uid') - 3])
                userNum = userNum + 1
            print (index, lineList.__len__(), 'file ' + str(order), allWeiboNum + weiboNum, userNum)
            index = index + 1

            # 按行存入新文件中，去掉末尾的\n，去掉空格
            line = line.strip()
            line = line.replace('\n', '', line.__len__())

            weibo_file_oneline.write(line)
            weibo_file_oneline.flush()

            if line.endswith('}') :
                line = line + '\n'

            weibo_file.write(line)
            weibo_file.flush()

        # 打印出来，随时查看运行中的信息
        allWeiboNum = allWeiboNum + weiboNum
        print u'计算的文件为：  ', file_path
        print u'该文件中微博数为：  ', weiboNum, u'  目前已统计微博总数为：  ', allWeiboNum

        f.close()

    # # 将结果写入文件中
    #
    # num_file = open('./result_files/计算结果.txt', 'wb+')
    #
    # num_file.write('__________________________________\n')
    # num_file.write('\nweiboCount：  ')
    # num_file.write(allWeiboNum)
    # num_file.write('\nuserCount：  ')
    # num_file.write(userNum)
    # num_file.write('\nweiboCount one average：  ')
    # num_file.write(allWeiboNum/userNum)
    # num_file.write('\n__________________________________\n')
    # num_file.write('\nmechines number：  12')
    # num_file.write('\naverage weibo number：  19604160\n')
    # num_file.write('\nspend time on crawling：  \n')
    # num_file.write('\n\t')
    # num_file.write(allWeiboNum/19604160)
    # num_file.write('\n__________________________________\n')
    # num_file.write('\ncalculate time：  ' )
    # num_file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # num_file.write('\n__________________________________\n')

    print u'统计和数据整合已完成...'
    print u'统计数据存放在  ./result_files/计算结果.txt  '
    print u'整合后的数据存放在  ./result_files/weibo_personInfo.json'

    weibo_file.close()
    weibo_file_oneline.close()
    num_file.close()





# weiboPersonInfoReference
微博个人信息爬取的相关内容
包括代码、文档、UID、爬取到的信息、统计信息等

## 个人信息爬取及数据处理部分

* sinaScrapy是爬取wap端新浪微博用户个人信息数据的爬虫
    * 非分布式，需要手动分割uid文件并分别启动爬虫脚本
    * 使用了cookie池、user-agent池，未使用ip池
    * 由于爬取wap端微博需要登陆，所以爬取效率较低
* dataProcessing存放着后期对数据处理的脚本
    * \> files < 目录中存放爬取后形成的json文件
    * \> result_files < 目录中存放处理后的json文件
    * \> calculateWeiboNum.py < 用于计算所有用户的微博数
    * \> FindFile.py < 用于测试时查找特定的用户信息，实际使用中可删除
    * \> saveToMongo.py < 用于将数据形成文本，同时存放到指定的mongodb中
    * \> backUpMongodb.py < 用于备份mongodb数据到mongodb中，用了分页查询和批量插入
    加快了转存的速度，速度约为3500条每秒。
    
    
## 微博信息爬取

* weibocontent就是进行微博爬取的脚本
* weibo信息爬取的代码在确保在不和后边集群机器连接的情况下再尝试（避免影响后边集群的爬取作业）
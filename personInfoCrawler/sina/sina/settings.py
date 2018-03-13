#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Scrapy settings for sinaPersonInfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

# 下面的三个配置是自动生成的，不用管
BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']

NEWSPIDER_MODULE = 'sina.spiders'

# 设置每次请求的间隔时间，这个是自定义的配置，不会自动生成
# 根据测试  单机 + 10 cookie 运行时，该配置设置0.5为极限频率（该频率在爬到了不到五万条数据时10个帐号就全部账号异常了，但是没有403和414，测试时间： 2017-9-17）
REQUEST_INTREVAL = 1.0

# 设置文件的读取位置，这个是自定义的配置，不会自动生成
INPUTFILE_LOCATION = 'e://input.txt'

# 设置数据的输出方式
ITEM_PIPELINES = {
    'sina.pipelines.TutorialPipeline': 300,
}

# 设置中间件
DOWNLOADER_MIDDLEWARES = {

    # 用户代理池的中间件
    "sina.middlewares.UserAgentMiddleware": 401,

    # cookie池的中间件，cookie池的功能暂时在spider中进行了，所以没有把cookie的功能作为middleware独立出来
    # "sina.middlewares.CookiesMiddleware": 402,

    # IP代理池的中间件，
    #"sina.middlewares.ProxyMiddleware" : 403,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sinaPersonInfo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Retry many times since proxies often fail
RETRY_TIMES = 3

# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 414, 10060, 10061]

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'

LOG_LEVEL = 'DEBUG'

LOG_FILE = "increment_comment.log"


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sinaPersonInfo.middlewares.SinapersoninfoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sinaPersonInfo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'sinaPersonInfo.pipelines.SinapersoninfoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

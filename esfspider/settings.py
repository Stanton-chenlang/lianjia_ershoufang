# Scrapy settings for esfspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'esfspider'

SPIDER_MODULES = ['esfspider.spiders']
NEWSPIDER_MODULE = 'esfspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'esfspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4412.3 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'esfspider.middlewares.EsfspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
    # 'esfspider.middlewares.EsfspiderDownloaderMiddleware': 543,
    # 'esfspider.middlewares.ProxyMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'esfspider.pipelines.EsfspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

TODAY = datetime.datetime.now()
# LOG_FILE_PATH = "../log/INFO_{}_{}_{}.log".format(TODAY.year, TODAY.month, TODAY.day)
LOG_FILE_PATH = "../log/WARNING_{}_{}_{}.log".format(TODAY.year, TODAY.month, TODAY.day)
# LOG_FILE_PATH = "../log/DEBUG_{}_{}_{}.log".format(TODAY.year, TODAY.month, TODAY.day)
# Set log level and log path
# LOG_LEVEL = "INFO"
LOG_LEVEL = "WARNING"
# LOG_LEVEL = "DEBUG"
LOG_FILE = LOG_FILE_PATH

# 对于JSON文件，需要设置编码格式
FEED_EXPORT_ENCODING = 'utf-8'

# 配置MySQL
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWD = '0712'
DB = 'housedata'
CHARSET = 'UTF8'
TABLE = 'lianjia'

# 图片保存路径
# IMAGES_STORE = 'D:/CODE/PycharmProjects/Second-hand housing data to climb/images'

# 设置代理IP
PROXIES = ['http://183.207.95.27:80', 'http://111.6.100.99:80', 'http://122.72.99.103:80',
           'http://106.46.132.2:80', 'http://112.16.4.99:81', 'http://123.58.166.113:9000',
           'http://118.178.124.33:3128', 'http://116.62.11.138:3128', 'http://121.42.176.133:3128',
           'http://111.13.2.131:80', 'http://111.13.7.117:80', 'http://121.248.112.20:3128',
           'http://112.5.56.108:3128', 'http://42.51.26.79:3128', 'http://183.232.65.201:3128',
           'http://118.190.14.150:3128', 'http://123.57.221.41:3128', 'http://183.232.65.203:3128',
           'http://166.111.77.32:3128', 'http://42.202.130.246:3128', 'http://122.228.25.97:8101',
           'http://61.136.163.245:3128', 'http://121.40.23.227:3128', 'http://123.96.6.216:808',
           'http://59.61.72.202:8080', 'http://114.141.166.242:80', 'http://61.136.163.246:3128',
           'http://60.31.239.166:3128', 'http://114.55.31.115:3128', 'http://202.85.213.220:3128']

# -*- coding: utf-8 -*-

# Scrapy settings for infospider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'infospider'

SPIDER_MODULES = ['infospider.spiders']
NEWSPIDER_MODULE = 'infospider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.25

LOG_FILE = 'view.log'
LOG_LEVEL = 'INFO'
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# Configure item pipelines
ITEM_PIPELINES = {
    'infospider.pipelines.JsonPipeline': 2,
    'ipspider.piplines.IpPipeline':2,
}

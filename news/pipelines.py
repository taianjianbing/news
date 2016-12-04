# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    pass


# 处理网易科技最新快讯
class WyKejiPipeline(object):
    def __init__(self):
        self.fh = open('wy/wykj.txt','w')

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        for i in range(len(title)):
            titlestd = title[i].strip().replace('\n','').replace('\t','')
            linkstd = link[i].strip()
            print(titlestd)
            print(linkstd)
            self.fh.write(titlestd+'\n'+linkstd+'\n')

    def close_spider(self):
        self.fh.close()

# 处理新华科技快讯

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    pass


# 处理网易科技最新快讯
class WyKejiPipeline(object):
    # def __init__(self):
    #     self.fhwy = open('wy/wykj.txt','w')
    #
    # def process_item(self, item, spider):
    #     title = item['title']
    #     link = item['link']
    #     for i in range(len(title)):
    #         titlestd = title[i].strip().replace('\n','').replace('\t','')
    #         linkstd = link[i].strip()
    #         print(titlestd)
    #         print(linkstd)
    #         self.fhwy.write(titlestd+'\n'+linkstd+'\n')
    #
    # def close_spider(self):
    #     self.fhwy.close()
    pass


# 处理新浪科技快讯
class SinaKejiPipeline(object):
    # def __init__(self):
    #     self.fhsina = open('sina/sinakj.txt','w')
    #
    # def process_item(self, item, spider):
    #     title = item['title']
    #     link = item['link']
    #     for i in range(len(title)):
    #         titlestd = title[i].strip().replace('\n','').replace('\t','')
    #         linkstd = link[i].strip()
    #         print(titlestd)
    #         print(linkstd)
    #         self.fhsina.write(titlestd+'\n'+linkstd+'\n')
    #
    # def close_spider(self):
    #     self.fhsina.close()
    pass

# 处理腾讯科技快讯
class QqKejiPipeline(object):
    def __init__(self):
        self.fhqq = open('qq/qqkj.txt','w')

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        for i in range(len(title)):
            titlestd = title[i].strip()
            linkstd = link[i].strip()
            print(titlestd)
            print(linkstd)
            self.fhqq.write(titlestd+'\n'+linkstd+'\n')

    def close_spider(self):
        self.fhqq.close()


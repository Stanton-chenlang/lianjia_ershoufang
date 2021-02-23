# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EsfspiderPipeline:
    def process_item(self, item, spider):
        return item


# 存储小区数据
class XiaoquPipelines(object):
    # 可选实现，做参数初始化等
    def __init__(self):
        pass

    # item (Item 对象) – 被爬取的item
    # spider (Spider 对象) – 爬取该item的spider
    # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
    # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider):
        pass


# 清洗小区数据（暂空）
class XiaoquPipelines2(object):
    def process_item(self, item, spider):
        pass

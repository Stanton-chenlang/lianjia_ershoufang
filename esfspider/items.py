# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoquItem(scrapy.Item):
    # define the fields for your item here like:
    xiaoqu_id = scrapy.Field()  # 小区编号
    xioaqu_area = scrapy.Field()  # 行政区
    xiaoqu_street = scrapy.Field()  # 街道
    unit_price = scrapy.Field()  # 小区均价
    xiaoqu_age = scrapy.Field()  # 建筑年代
    xiaoqu_type = scrapy.Field()  # 建筑类型
    ppty_expenses = scrapy.Field()  # 物业费用
    ppty_company = scrapy.Field()  # 物业公司
    developer = scrapy.Field()  # 开发商
    build_num = scrapy.Field()  # 楼栋总数
    house_num = scrapy.Field()  # 房屋总数
    house_url = scrapy.Field()  # 小区在售二手房url


class EsfspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

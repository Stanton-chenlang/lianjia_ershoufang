# import re
import json
# import scrapy
from scrapy import Spider, Request
from lxml import etree


class TestxiaoquSpider(Spider):
    name = 'testxiaoqu'
    allowed_domains = ['www.bj.lianjia.com/xiaoqu', 'www.bj.lianjia.com']
    areas = {#'dongcheng': '东城'
               # 'xicheng': '西城',
               # 'chaoyang': '朝阳',
               # 'haidian': '海淀',
               # 'fengtai': '丰台',
               # 'shijingshan': '石景山',
               # 'tongzhou': '通州',
               # 'changping': '昌平',
               # 'daxing': '大兴',
               # 'yizhuangkaifaqu': '亦庄开发区',
               # 'shunyi': '顺义',
               # 'fangshan': '房山',
               # 'mentougou': '门头沟',
               # 'pinggu': '平谷',
               # 'huairou': '怀柔',
               # 'miyun': '密云',
               'yanqing': '延庆'
               }

    def start_requests(self):
        for area in list(self.areas.keys()):
            url = "https://bj.lianjia.com/xiaoqu/" + area + "/"
            yield Request(url=url, callback=self.parse, meta={'area': area})  # 用来获取页码
    """
    def parse(self, response):
        selector = etree.HTML(response.text)
        streetname_list = selector.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div/div[2]/a")  # 返回关于街道名称的列表
        streeturl_list = selector.xpath("/html/body/div[3]/div[1]/dl[2]/dd/div/div[2]/a/@href")  # 返回关于街道url的列表
        street_list = dict(zip(streeturl_list, streetname_list))
        # print(streeturl_list)

        for k,v in street_list.items():  # 对每个街道url进行抓取
            url_street = "https://bj.lianjia.com" + k
            # print(url_street, k, v.text, type(v))
            yield Request(url=url_street, callback=self.parse_xiaoqu, dont_filter=True, errback=self.errback,
                          meta={'street_url': k, 'street_name': v.text, 'area': response.meta['area']})

    def parse_xiaoqu(self, response):  # 抓取所有街道url
        # print(response.meta['region'], street_name)
        selector = etree.HTML(response.text)
        sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]  # 返回的是字符串字典 当前街道共有页数
        sel = json.loads(sel)  # 转化为字典
        total_pages = sel.get("totalPage")

        for i in range(int(total_pages)):  # 当前街道url下，循环跳转下一页https://bj.lianjia.com/xiaoqu/huairouchengqu1/pg2/?from=rec
            url_page = "https://bj.lianjia.com{}pg{}/?from=rec".format(response.meta['street_url'], str(i + 1))
            # print("url_page: ", url_page)
            yield Request(url=url_page, callback=self.parse_id, dont_filter=True, errback=self.errback,
                          meta={'street_name': response.meta['street_name'], 'area': response.meta['area']})

    def parse_id(self, response):  # 抓取所有小区id
        selector = etree.HTML(response.text)
        xiaoqu_code_list = selector.xpath('/html/body/div[4]/div[1]/ul/li/@data-housecode')  # 获取小区的id，返回该街道url下第几页的所有小区id

        for co in xiaoqu_code_list:
            url_xiaoqu = "https://bj.lianjia.com/xiaoqu/" + co
            # print("url_xiaoqu", url_xiaoqu)
            yield Request(url=url_xiaoqu, callback=self.parse_content, dont_filter=True, errback=self.errback,
                          meta={'xiaoqu_id': co, 'street_name': response.meta['street_name'], 'area': response.meta['area']})

    def parse_content(self, response):  # 抓取每个小区的详细信息
        xiaoqu_id = response.meta['xiaoqu_id']
        selector = etree.HTML(response.text)
        try:  # 返回小区均价
            unit_price = selector.xpath('/html/body/div[6]/div[2]/div[1]/div/span[1]')[0].text
        except IndexError:
            unit_price = "暂无信息 "
        try:  # 返回建筑年代
            xiaoqu_age = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/span[2]')[0].text
        except IndexError:
            xiaoqu_age = "暂无信息 "
        try:  # 返回建筑类型
            xiaoqu_type = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[2]/span[2]')[0].text
        except IndexError:
            xiaoqu_type = "暂无信息 "
        try:  # 返回物业费用
            ppty_expenses = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[3]/span[2]')[0].text
        except IndexError:
            ppty_expenses = "暂无信息 "
        try:  # 返回物业公司
            ppty_company = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[4]/span[2]')[0].text
        except IndexError:
            ppty_company = "暂无信息 "
        try:   # 返回开发商
            developer = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[5]/span[2]')[0].text
        except IndexError:
            developer = "暂无信息 "
        try:  # 返回楼栋总数
            build_num = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[6]/span[2]')[0].text
        except IndexError:
            build_num = "暂无信息 "
        try:  # 返回房屋总数
            house_num = selector.xpath('/html/body/div[6]/div[2]/div[2]/div[7]/span[2]')[0].text
        except IndexError:
            house_num = "暂无信息 "

        # 返回小区在售二手房url
        house_url = 'https://bj.lianjia.com/ershoufang/c' + xiaoqu_id + "/"
        # 返回小区所在街道
        xiaoqu_street = response.meta['street_name']
        # 返回小区所属行政区
        xioaqu_area = response.meta['area']

        print({
            '小区编号': xiaoqu_id,
            '行政区': xioaqu_area,
            '街道': xiaoqu_street,
            '小区均价': unit_price,
            '建筑年代': xiaoqu_age,
            '建筑类型': xiaoqu_type,
            '物业费用': ppty_expenses,
            '物业公司': ppty_company,
            '开发商': developer,
            '楼栋总数': build_num,
            '房屋总数': house_num,
            '小区在售二手房url': house_url
        })

    def errback(self, failure):
        self.logger.error(repr(failure))
    """

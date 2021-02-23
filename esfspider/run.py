# -*- coding: utf-8 -*-
# @Time : 2021/2/19 0:26
# @Author : Stanton
# @File : ershoufangScrappy/run.py
from scrapy import cmdline


class Run:
    def __init__(self, name):
        self.spider_name = name

    def parse_cmd(self):
        cmd = 'scrapy crawl ' + self.spider_name
        cmdline.execute(cmd.split())

    def parse_cmd_out(self):
        cmd = 'scrapy crawl {} -o {}.csv'.format(self.spider_name, self.spider_name)
        cmdline.execute(cmd.split())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run = Run(name='testxiaoqu')
    run.parse_cmd()

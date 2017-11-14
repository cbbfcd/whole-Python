# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-14 22:52:40
# @Last Modified by:   28906
# @Last Modified time: 2017-11-14 23:13:45
# @Description: 实现同时执行多个爬虫。重写crawl.py文件
import os
from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import arglist_to_dict
from scrapy.utils.python import without_none_values
from scrapy.exceptions import UsageError

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return "[options] <spider>"

    def short_desc(self):
        return "Run all spider"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[],metavar="NAME=VALUE", help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE", help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT", help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)
        if opts.output:
            if opts.output == '-':
                self.settings.set('FEED_URI', 'stdout:', priority='cmdline')
            else:
                self.settings.set('FEED_URI', opts.output, priority='cmdline')
            feed_exporters = without_none_values(self.settings.getwithbase('FEED_EXPORTERS'))
            valid_output_formats = feed_exporters.keys()
            if not opts.output_format:
                opts.output_format = os.path.splitext(opts.output)[1].replace(".", "")
            if opts.output_format not in valid_output_formats:
                raise UsageError("Unrecognized output format '%s', set one"
                                 " using the '-t' switch or as a file extension"
                                 " from the supported list %s" % (opts.output_format, tuple(valid_output_formats)))

            self.settings.set('FEED_FORMAT', opts.output_format, priority='cmdline')
    # 重写 run 方法，实现run多个爬虫文件。
    def run(self, args, opts):
        # 获取爬虫列表
        spd_loader_list = self.crawler_process.spider_loader.list()
        # 遍历
        for spname in spd_loader_list or args:
        	self.crawler_process.crawl(spname, **opts.spargs)
        	print('启动爬虫: ' + spname)
        self.crawler_process.start()

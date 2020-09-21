"""
https://www.soogif.com/shareSatin
爬取 热门git图片 https://www.soogif.com/hotGif?start=0&size=20 每页最大数量为20 当前已下载前2000, 后续i需从100开始
"""
import scrapy
import json
from ..items import GifspiderItem


class SoGifSpider(scrapy.Spider):
    name = 'so-gif'

    def __init__(self, start_page=0, end_page=100, *args, **kwargs):
        super(SoGifSpider, self).__init__(*args, **kwargs)
        self.start_page = int(start_page)
        self.end_page = int(end_page)

    def start_requests(self):
        base_url = "https://www.soogif.com/hotGif?start={}&size={}"
        for i in range(self.start_page, self.end_page):
            url = base_url.format(i * 20, i * 20 + 20)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, resp):
        results = json.loads(resp.text)
        for result in results['data']['result']:
            print("title: {}, url: {}".format(result['title'], result['gifurl']))
            filename = result['title']
            item = GifspiderItem(name=filename, url=result['gifurl'])
            yield item

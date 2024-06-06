import scrapy
from first_scrapy.items import FirstScrapyItem


class XuexiaoSpider(scrapy.Spider):
    name = "xuexiao"
    allowed_domains = ["www.qzqgxy.com"]
    start_urls = ["http://www.qzqgxy.com"]

    def parse(self, response):
        #  解析网页提取数据，使用xpath
        rep_list = response.xpath('//div[@class="list2"]/ul/li')
        data_list = []
        for i in rep_list:
            title = i.xpath('a/text()').get()  # 用get方法来获取Selector 里面的数据
            href = i.xpath('a/@href').get()  # 同理
            if title and href:
                # 创建一个Item实例，并填充数据
                item = FirstScrapyItem()
                item['title'] = title
                item['href'] = href
                # 使用yield关键字产出Item
                yield item



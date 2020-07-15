import scrapy
from CatchAnm.items import CatchanmItem

class CatchAnm_spider(scrapy.Spider):
    name = 'catchAnm'
    allowed_domain = ['https://tieba.baidu.com/']
    urls = input('请输入需要爬取的百度贴吧网页地址:\n')
    start_urls = [urls]

    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        items =[]
        sites = sel.xpath('//cc/div')
        for site in sites:
            item = CatchanmItem()
            item['anm_url']= site.xpath('img[@class="BDE_Image"]/@src').extract()
            if len(item['anm_url']) != 0 :
                items.append(item)

        return items
            

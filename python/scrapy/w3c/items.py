import scrapy
#抓取页面中的名称，链接，描述
class W3CItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()
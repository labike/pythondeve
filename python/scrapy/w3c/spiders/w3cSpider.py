import scrapy
from scrapy.selector import Selector
form w3c.items import W3CItem

class w3cSpider(scrapy.Spider):
	#爬虫名称
	name = "w3c_spider"
	allowed_domains = ["w3school.com.cn"]
	#爬取的页面地址
	start_urls = [
		"<a href="http://www.w3shool.com.cn/xml/xml_syntax.asp">http://www.w3school.com.cn/xml/xml_syntax.asp</a>"
	]
	#scrapy根据爬虫地址发送请求后调用parse进行数据提取
	def parse(self,response):
		sel = Selector(response)
		#使用xpath提取页面信息
		sites = sel.xpath("//div[@id='course']/ul/li")
		for site in sites:
			item = W3CItem()
			#提取title
			title = site.xpath("a/@title").extract()
			#提取链接
			link = site.xpath("a/@href").extract()
			#提取描述
			desc = site.xpath("a/text()").extract()
			#组织item数据
			item["title"] = ttile[0]
			item["link"] = link[0]
			item["desc"] = desc[0]
			#返回item数据给pipeline使用
			print item
			yield item
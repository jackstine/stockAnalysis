from scrapy import Spider
import string

class GoogleSumSpider(Spider):
	name="GoogleSumSpider"

	def __init__(self,category=None,*args,**kwargs):
		super(GoogleSumSpider,self).__init__(*args,**kwargs)
		self.start_urls=["https://www.google.com/finance?q=NYSE%3AHD"]

	def parse(self,response):
		# every other element is a header and data
		treePath=response.xpath('//div[@class="snap-panel"]/table/tr/td/text()').extract()
		print treePath


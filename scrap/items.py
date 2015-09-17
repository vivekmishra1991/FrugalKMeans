import scrapy

class frugalMeansItem(scrapy.Item):
	name = scrapy.Field()
	addr = scrapy.Field()
	
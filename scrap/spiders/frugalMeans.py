from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from scrap.items import frugalMeansItem

class frugalMeansRest(Spider):
	name = "frugalMeans"
    #we are scraping data from indian food website here
	allowed_domains = ["YOUR_DOMAIN"]
	start_urls = [
		"YOUR_URL_HERE",
	]
        

    
        def parse(self, response):
    	   #html/body/div[6]/div/div/div/div/section/div/div/div/dd/div[2]/a/@href
    	    url_list=response.xpath('/html/body/div[6]/div/div/div/div/section/div/div/div/dd/div[1]/a/@href').extract()

            #url_list=url_list[1:3]
            for url in url_list:
                yield Request(url, callback=self.parse_dir_contents)
            

        def parse_dir_contents(self, response):
        
            sel = Selector(response)
            sites = sel.xpath('//*[@id="mainframe"]/div/div[1]/div[1]')
            items=[] 

            for site in sites:
                item = frugalMeansItem()
                item['name'] = site.xpath('a[1]/text()').extract()
                print item['name']
                item['addr'] = site.xpath('span[2]/text()').extract()
                #     item['description'] = site.xpath('//*[@id="mainframe"]/div[3]/div[1]/div/span[2]')
                items.append(item)
                
            return items 
 

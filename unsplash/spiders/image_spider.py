import scrapy 
from scrapy_selenium import SeleniumRequest

from ..items import UnsplashItem

class ImageSpider(scrapy.Spider):
    name = 'img_spider'
    
    
    def start_requests(self):
        category = input("Enter image Category: ")
        url = 'https://unsplash.com/s/photos/'+category
        yield SeleniumRequest(url=url, callback=self.parse ,wait_time=10)

    def parse(self,response):
        row_img_url = response.xpath('//div[@class="MorZF"]/img/@src').getall()
        # row_img_url = response.xpath("//div[@class='quote']/span[@class='text']").extract()
        # title = response.xpath('//div[@class="zmDAx"/a/@title').getall()

        # print(title)
        # if title is not None:
        #     img_title.append(title)
        # else:
        #     img_title.append(num)

        clean_url = []
        for img_url in row_img_url:
            clean_url.append(response.urljoin(img_url))

        yield{
            'image_urls': clean_url
        }

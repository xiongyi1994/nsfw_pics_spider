import scrapy
import os

class nsfw_22aap(scrapy.Spider):
    name = '22aap'
    x = 1
    def start_requests(self):
        yield scrapy.Request(url='http://www.22aap.com/html/article/index14710.html', callback=self.parse)

    def parse(self, response):
        imgs = response.xpath("//*[contains(@class,'content')]//img//@src").extract()
        for img_url in imgs:
            print img_url
            yield scrapy.Request(url=img_url, callback=self.download)
        next_page = response.xpath("//*[contains(@class,'pagea')]//@href").extract()
        if len(next_page) > 1:
            next_page = next_page[1]
            next_page = "http://www.22aap.com" + next_page
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def download(self, response):
        filename = os.path.join("/Users/xiongyi/Downloads/images", str(self.x) + ".jpg")
        self.x += 1
        with open(filename, "wb") as f:
            f.write(response.body)

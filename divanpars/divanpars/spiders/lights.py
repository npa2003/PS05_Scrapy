import scrapy


class LightsSpider(scrapy.Spider):
    name = "lights"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.LlPhw')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.q5Uds span::text').get(),
                'url': light.css('div.lsooF link').attrib['href']
            }

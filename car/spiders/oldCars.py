import scrapy
from car.items import CarItem


class OldcarsSpider(scrapy.Spider):
    name = "oldCars"
    allowed_domains = ["sanbonbanh.com"]
    start_urls = ["https://sanbonbanh.com/"]

    def start_requests(self):
        with open('car\spiders\page_number.txt', 'r') as file:
            i = int(file.read())
        domain = 'https://sanbonbanh.com/sellcar/page-{}/'.format(i)
        yield scrapy.Request(url=domain, callback=self.parse_link)
        print('----------------------------------------------', i)
        with open('car\spiders\page_number.txt', 'w') as file:
            file.write(str(i + 1))

        
    def parse_link(self, response):
        for i in range(1, 21):
            str = 'body > section.product-listing.page-section-ptb > div > div > div.col-lg-8.col-md-7.bg-white > div.list-group > div:nth-child({}) > div > div.col-lg-8.col-md-12 > div > div.car-title > a::attr(href)'.format(i)
            link = response.css(str).extract_first()

            yield scrapy.Request(response.urljoin(link), callback=self.parse)

    def parse(self, response):
        item = CarItem()
        item['name'] = response.xpath(
            '/html/body/section[2]/div/div[1]/div[1]/h3/text()').extract_first()
        item['yom'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[7]/strong/text()').extract_first() 
        item['price'] = response.xpath(
            '/html/body/section[2]/div/div[1]/div[2]/div[1]/strong/text()').extract_first() 
        item['origin'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[5]/strong/text()').extract_first() 
        item['color'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[4]/td/text()').extract_first() 
        item['KMtraveled'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[8]/strong/text()').extract_first() 
        item['status'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[2]/strong/text()').extract_first() 
        item['doorNumber'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td/text()').extract_first() 
        item['seatNumber'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td/text()').extract_first() 
        item['engine'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[9]/strong/text()').extract_first() 
        item['gear'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[5]/td/text()').extract_first() 
        item['fuelConsumption'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[8]/td/text()').extract_first() 
        
        yield item
import scrapy
from car.items import CarItem
import pandas as pd
import numpy as np


class OldcarsSpider(scrapy.Spider):
    name = "oldCars"
    allowed_domains = ["sanbonbanh.com"]
    start_urls = ["https://sanbonbanh.com/"]

    def start_requests(self):
        # s = ""
        # e = ""
        pages = []
        for i in range(17,19): 
            domain = 'https://sanbonbanh.com/sellcar/page-{}/'.format(i)
            pages.append(domain)

        for page in pages:
            yield scrapy.Request(url=page, callback=self.parse_link)
    def parse_link(self, response):
        for i in range(1, 21):
            str = 'body > section.product-listing.page-section-ptb > div > div > div.col-lg-8.col-md-7.bg-white > div.list-group > div:nth-child({}) > div > div.col-lg-8.col-md-12 > div > div.car-title > a::attr(href)'.format(i)
            #      body > section.product-listing.page-section-ptb > div > div > div.col-lg-8.col-md-7.bg-white > div.list-group > div:nth-child(2) > div > div.col-lg-8.col-md-12 > div > div.car-title > a
            #      body > section.product-listing.page-section-ptb > div > div > div.col-lg-8.col-md-7.bg-white > div.list-group > div:nth-child(1) > div > div.col-lg-8.col-md-12 > div > div.car-title > a
            link = response.css(str).extract_first()

            yield scrapy.Request(response.urljoin(link), callback=self.parse)

    def parse(self, response):
        item = CarItem()
        item['name'] = response.xpath(
            '/html/body/section[2]/div/div[1]/div[1]/h3/text()').extract_first() 
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
        # item['seatNumber'] = response.xpath(
        #     '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td/text()').extract_first() 
        item['engine'] = response.xpath(
            '/html/body/section[2]/div/div[2]/div[2]/div/div/ul/li[9]/strong/text()').extract_first() 
        item['gear'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[5]/td/text()').extract_first() 
        item['fuelConsumption'] = response.xpath(
            '/html/body/section[2]/div/div[3]/div[1]/div[1]/div[1]/table/tbody/tr[8]/td/text()').extract_first() 
        
        yield item


df = pd.read_csv('D:\DEBeginner\Project2\car\car.csv')

df = df[['name','price','origin','status','KMtraveled','color','doorNumber','engine','fuelConsumption']]
df.to_csv('car/car.csv', sep='\t', encoding='utf-8')
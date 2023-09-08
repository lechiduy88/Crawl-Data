# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() # Tên xe
    yom = scrapy.Field() #Năm sản xuất 
    price = scrapy.Field() # Giá xe
    origin = scrapy.Field() #Xuất xứ 
    color = scrapy.Field() # Màu xe
    KMtraveled = scrapy.Field() #Số km đã đi
    status = scrapy.Field() #Tình trạng
    doorNumber = scrapy.Field() #Số cửa
    seatNumber = scrapy.Field() #Số chỗ ngồi 
    engine = scrapy.Field() # Động cơ
    gear = scrapy.Field() #Hộp số
    fuelConsumption = scrapy.Field() #Mức độ tiêu thụ nguyên liệu
    pass

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Carbon38Item(scrapy.Item):
    breadcrumbs = scrapy.Field()
    image_url = scrapy.Field()
    brand = scrapy.Field()
    product_name = scrapy.Field()
    price = scrapy.Field()
    reviews = scrapy.Field()
    colour = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()
    sku = scrapy.Field()
    product_id = scrapy.Field()
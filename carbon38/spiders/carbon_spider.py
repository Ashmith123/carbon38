import scrapy
from carbon38.items import Carbon38Item

class CrawlingSpider(scrapy.Spider):
    name = "carbon38"
    allowed_domains = ["carbon38.com"]
    start_urls = ["https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1"]

    def parse(self, response):
        products = response.css('div.ProductItem__Info')
        for product in products:
            product_url = product.css('h2.ProductItem__Title a').attrib['href']
            yield response.follow(product_url, self.parse_product)

        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_product(self, response):
        item = Carbon38Item()
        item['breadcrumbs'] = response.css('ul.Breadcrumb__List li::text').getall()
        item['image_url'] = response.css('div.Product__SlideItem--image img::attr(src)').get()
        item['brand'] = response.css('span.ProductMeta__Vendor::text').get()
        item['product_name'] = response.css('h1.ProductMeta__Title::text').get()
        item['price'] = response.css('span.ProductMeta__Price Price::text').get()
        item['reviews'] = response.css('span.ProductMeta__Reviews::text').get()
        item['colour'] = response.css('span.ProductMeta__OptionLabel::text').get()
        item['sizes'] = response.css('ul.ProductForm_Option.ProductForm_Option--labelled input::attr(value)').getall()
        item['description'] = response.css('div.ProductMeta__Description span::text').getall()
        item['sku'] = response.css('span.ProductMeta__Sku::text').get()
        item['product_id'] = response.css('span.ProductMeta__ProductId::text').get()
        yield item